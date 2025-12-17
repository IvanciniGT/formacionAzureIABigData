
Consideraciones sobre los procesos que hemos montado en databricks:
1. En nuestro caso, hemos metido las palabras prohibidas en una lista hardcodeada.
   Esto es un sinsentido. Lo suyo sería tenerlo en una tabla (HIVE + DELTA ). 
   En SparkSQL Se pueden hacer JOINS. En este caso, quizás un join no sea lo más adecuado.

    Escenario donde si tiene sentido:
    Me llega un CODIGO POSTAL en el tweet.
    Tengo una tabla con CODIGOS POSTALES e información de GEOPOSICIONAMIENTO (lat,lon, radio)
    Hago un JOIN. IDEAL... Aunque:
    - Aunque estemos trabajando con SQL, no tenemos una BBDD.
    - Por debajo la infra sigue siendo la que ofrece SPARK : RDDs (colecciones de datos en memoria, persistidas a ficheros)
    
       - Algoritmos de resolución de JOINS en SPARK:
         - Merge Join       (2 tablas ordenadas por la clave de join, que se bvan procesando en paralelo)
                  ID CAMPOA CAMPOJOIN          ID(CAMPOJOIN) CAMPOB
                  1   AAA     1                1             100 
                  2   CCC     2                2             200
                  3   EEE     2                3             300  *
                  4   GGG     3  *             4             400
         - Nested Loop Join (Lookup Join)
         - Hash Join
                    TABLA A x TABLA B 
                    La tabla A la puedo partir en 50 cachos... y mandar un cacho a cada nodo del cluster
                    La tabla B la tengo que mandar entera a cada nodo del cluster.
    Spark NO ES UNA BBDD por mucho que escriba código SQL... no tengo índices, los algoritmos de join son muy limitados y tengo que distribuir las tablas entre los nodos del cluster.... y una de ellas va a tener que ir entera a cada nodo (MEMORIA RAM)

    Para algo como los CP no hay problema. Son 4 datos (100.000 + info asociada). 5 MBs - 2 GBs

    Aquí sale de nuevo un concepto que comenté el primer día: ETL y sus variantes
    Hay veces que me interesa más que Transformas en SPARK (T) 
        E (Fichero) -> T (Spark) -> L (Tabla Delta)
        E (Kafka) -> T (Spark) -> L (Azaure CosmosDB)
        En ocasiones ciertas trasnformaciones son más sencillas/convenientes de hacer en otros sitios
        +
        Quizás si tengo que cruzar tablas muy grandes, me interesa hacer un preprocesado previo (ETL) cargar en una BBDD y ahí hacer el JOIN, que será mucho más eficiente que el que puedo hacer aquí!

3. En el ejemplo nuestro,
   Capa bronze -> Guardamos los tweets tal cual llegan (INCREMENTAL en delta) + fecha de ingesta
   Capa silver -> Procesamos los tweets para extraer hashtags, menciones, urls + marcar si tienen palabrotas o no (Me interesa guardar en incremental en delta)
   Capa gold   -> Hacemos agregaciones (pero también me interesa guardar en incremental en delta)
                  Puedo agrupar los hashtags por 5 minutos
                  Y la guardo en delta incremental

    Quién sea que vaya a usar eso, hará lo que le interese.
       Capa gold (agrupación de hashtags por 5 minutos) -> otro proceso a capa gold 
       (trending topic por hora) -> Aquí no hay append... aquí hay overwritte (sobreescritura)
       Aunque quiero tabla delta (porque quiero versionado, quiero ver el histórico de cómo han ido evolucionando los trends)


2. En capa bronze y silver no quitamos datos
   - Capa bronze, solo completamos con metadatos (fecha de ingesta, origen de datos, creación de un id único...) -> Guardar los tweets tal cual los recibimos, pero con fecha de ingesta, id único...
   - Capa silver, procesamos datos... para transformarlos según interese -> 
     --> Sacar los hashtags + infor de si contienen palabras de mierda o no
     --> Sacar las menciones
     --> Sacar las urls 
   - Capa gold, ya sí que hacemos agregaciones, cálculos... -> Número de tweets por día, número de tweets por usuario, número de tweets que contienen palabrotas...
     --> Calculo los trends (hashtags más usados por día, quitando las palabrotas)
     --> Calculo los usuarios que escriben muchas palabrotas al dia
     --> Calculo los usuarios más mencionados por día

     Esto da lugar a un pipeline arborescente:

                    Capa Bronze
                        |
        ---------------------------------
        |               |               |
        Capa Silver    Capa Silver    Capa Silver
        (hashtags)     (menciones)     (urls)
        |               |               |
      Capa Gold      Capa Gold      Capa Gold
      (trends)      (usuarios)     (estadísticas urls)
      (etc...)        (etc...)        (etc...)


El origen de datos... Spark nos da algunas utlidades... aunque pocas:
- De ficheros(csv, json, parquet, avro, etc)   <--- Esto es lo que se usa en modo batch
                         ^^^^^^^ (en Databriks... evolucionados a Delta Lake)
- De bases de datos (jdbc)                      (NO LO USAMOS MUCHO)
- De colas de mensajería (kafka, etc)
   ^^^ Si voy en modo Streaming (tweets)
    El modo streaming de Spark es en realidad lanzar un montón de procesos batch cada X segundos


Parquet es lo que guardamos en el DATALAKE.... BARATO !!!

Las BBDD desperdician espacio a lo animal!
Una tabla se guarda en bloques de datos, dentro de un fichero (8Kbs)
Y en cada bloque se dejka espacio sin usar intencional, para que si se hace un update de un registro y crece en tamaño, siga entrando en el bloque.
De lo contrario sería un desastre: ROW MIGRATION (mover filas entre bloques/página, fragmentación, etc)

Hay cosas más sangrantes: POSTGRES
En postgres, los datops de cada fila se guardan en bloques de 8 bytes (PADDING DE POSGRES)
Hay que jugar al tetris con el orden de las columnas para que no haya padding y se aproveche bien el espacio.

Columna SMALLINT DATE INT
           2       4   4 -> 10 bytes
           Pero en postgres, asi guardado ocuparía 12
           XXxxxx  |kkkk
        DATA INT SMALLINT DATE
          4  4.    2
          Xxkkxx | xxxx

Esto no significa que no necesitemos en ocasiones conectar con otros sitemas (BBDD tradicionales, MongoDB, etc) En estos casos, lo normal es esa parte del proceso ETL hacerla fuera de Spark.
En el caso de AZURE,... ahí es donde entra DataFactory (ADF)

En DataFactory definimos:
 - Ingesta de datos desde BBDD tradicionales, MongoDB, etc
 - Pipelines
 - Orquestadores de procesos ETL

Muchas veces montamos una orquestación en ADF que carga datos desde BBDD tradicionales a un DATALAKE (ficheros parquet) -> Y luego lanzamos un proceso Spark (en Databricks) que lee esos ficheros parquet y hace las transformaciones que nos interesen.
O los mando online sin pasar por ficheros y Spark lo guarda ya en parquets en el DATALAKE.

---

# IA en Azure

Somos una empresa que ofrece un determinado tipo de servicio... y emitimos facturas/tickets a los clientes.
Y esas facturas tienen un formato determinado... que puede cambiar! O tenemos varios modelos de facturas.

Soy una empresa de transportes... y doy billetes de tren, avión, autobús.

Y monto una app web para reclamaciones.
El cliente sube una foto del ticket/factura/billete.

De ese documento (imagen... que puede venir.. como dios quiera: borrosa, torcida, con cosas alrededor, etc) quiero extraer:
 - Fecha
 - Importe
 - NIF/CIF
 - Número de factura/billete/servicio
 - Otros datos que me interesen

Esto es lo que antes hacíamos con OCRs (Reconocimiento óptico de caracteres)
El OCR tiene unas limitaciones brutales.
 - Necesita que la imagen esté bien tomada
 - Necesita que el texto esté en un formato legible (fuente, tamaño, etc)
 - Necesita que el documento esté bien encuadrado, sin cosas alrededor, etc
 - Si lo que quier es sacar datos distintos del documento, que las zonas donde están esos datos estén bien definidas y no cambien

Esto hoy en día es cuestión de 10 minutos montarlo con los servicios de IA de Azure.

---

Soy un hospital. Y los médicos van generando informes médicos (texto) de los pacientes.
Quiero montar un sistema que me lea esos informes y me extraiga:
 - Diagnóstico
 - Tratamiento
 - Medicación
 - Sintomas
 - Otros datos que me interesen

Este es un poco más complejo de montar... pero no tanto más.

--- 
Todo este tipo de cosas son las puedo montar con la forja de servicios de IA de Azure:
 - Servicios preentrenados (Vision, Language, Speech, Decision) que puedo usar tal cual ...
 - y lo más habitual: que los personalice (Custom Vision, Language Studio, Speech Studio)

La pruesta en producción es estos sistemas es muy sencilla en AZURE.
La inversión de tiempo está en la preparación de los datos para personalziar los modelos.
Cuantos más datos y más organizados, mejor resultado tendrá el modelo.

---

# Los modelos de IA son entes vivos

Vamos generando versiones de ellos.
La primera versión es posible que sea un poco castaña. (quizás hace bien el trabajo en un 80-90% de los casos) Para primera versión no está mal.... pero no es suficiente.

Hacer el día 1 un modelo de IA y esperar que funcione guay es irrealista.

Todo el control de versiones de los modelos es fundamental.

Y a eso también nos ayuda Azure con la forja.

La idea es:
- Elegimos el tipo de IA que queremos montar:
 - Vision
 - Language
 - Speech
 - Bot
- Una vez elegido, eligimos si usamos una subcategoría.
  De cada una de ellas tengo varias:
  - Vision:
   - Custom Vision
   - Form Recognizer
   - Video Analyzer
   - Etiquetado de imágenes
  - Language:
   - QnA Maker
   - Translator
   - Análisis de sentimientos
   - Extracción de entidades
   - Resumen de texto
   - Identificación de características
- Le preparo datos de entrenamiento
- Entreno el modelo
- Evalúo el modelo
- Despliego el modelo

Al final, un modelo de IA (que todos estos son redes neuronales complejos) es una función de programación que dados unos datos de entrada (foto, texto, audio) devuelve unos datos de salida (foto, audio, texto)

Cuando desplegamos uno de estos modelos en Azure, lo que se monta es un servicio REST (API REST) al que le puedo hacer peticiones (POST) con los datos de entrada y me devuelve los datos de salida. Internamente está ejecutando el modelo de IA.

Eso son cosas por separado:
- Servicios REST (APIs REST)
- Modelos de IA (redes neuronales complejas)

De hecho puedo sobree el mismo servicio REST ir cambiando el modelo de IA que hay detrás.

Vamos a tener además la posibilidad de hacer despliegues en distintos entornos:
 - Desarrollo
 - Pruebas
 - Producción
Para según que tipo de modelo, también tengo algunas utilidades para preparar la información de entrenamiento, me facilitan: 
- Etiquetado de datos (Labeling)
- Clasificación de datos

---

Fotografias de objetos.. quiero identificar el tipo de objeto que es.
Soy una empresa que fabrica lavadoras y ofrezco en mi web FAQ... y pido al usuario foto de su producto (lavadora)... y de la foto saco el modelo.

Entreno ese modelo dándole fotos de lavadoras de distintos modelos. Y voy diciendo a cada foto qué modelo es: Clasificando las fotos.

En realidad... no solemos plantear este mundo asi!

---

# DEVOPS

Es una cultura, es una filosofía, es un movimiento en pro de la automatización de trabajos.
En croncreto de todo lo que hay automatizable entre el DEV-> OPS

Devops es... Chicos: Vamos a AUTOMATIZAR TODO LO AUTOMATIZABLE!!!

Pipelines de CI/CD (Integración continua / Despliegue continuo)
 - Cada vez que hago un cambio en el código fuente, se lanza un proceso automático que:
   - Compila el código
   - Ejecuta tests automáticos
   - Si todo va bien, empaqueta el código
   - Despliega el código en un entorno de pruebas
   - Ejecuta tests automáticos en el entorno de pruebas
   - Si todo va bien, despliega el código en producción


Ese concepto de DEVOPS lo puedo aplicar a los modelos de IA que vayamos generando.
Al fin y al cabo, los modelos de IA no son sino programas, con versiones... que tengo que desarrollar, probar, desplegar.... casí igual... porque tienen sus peculiaridades.

Hay un concepto que se llama MLOPS (Machine Learning Operations)... y es la extensión de DEVOPS al mundo de la IA.

La idea es ir paso a paso con estos proyectos.

Tengo ya una web que da servicio a los clientes, para reclamaciones.
Y ahñi tengo un formulario de los de toda la vida:
- Ponga su DNI
- Ponga su nombre
- Ponga el número de billete

Que se escriben a mano.

Ahora monto un modelo de IA que lee la foto del billete y extrae esos datos automáticamente....
Pero esa primera version es regulinga! Atina "bastante"!

Que hago, una versión de la app, en la que tras capturar la foto del billete, le muestro al usuario el formulario relleno con los datos que ha extraído el modelo de IA.
Y le pido que los revise y corrija si es necesario.
Y los datos finales no los uso solamente para grabarlos en la BBDD, sino que los uso también para retroalimentar el modelo de IA. Esa nueva foto, con los datos que un usuario ha corregido, la uso para entrenar de nuevo el modelo de IA y sacar una nueva versión mejorada.

De esta forma, el modelo de IA va mejorando con el tiempo.... el solito, en realidad no... en realidad porque le voy pasando muchos datos nuevos, con correcciones guays!... pero como está automatizado... parece que el modelo de IA va mejorando solito! SIN INTERVENCIÓN HUMANA!

Cuando el modelo geneera datos que ya prácticamente no necesitan corrección humana, entonces ya puedo montar una versión de la app que no pida confirmación al usuario... y el modelo de IA ya funciona solo!

---

 - Servicios de IA avanzada (Azure OpenAI Service)