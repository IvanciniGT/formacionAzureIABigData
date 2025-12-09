
# Vocabulario

## BBDD - Base de Datos

No como programa. Sino como conjunto de datos organizados que estan siendo gestionados.
Son datos vivos. Habitualmente los tenemos en los entornos de producción.

Tenemos distintas apps que van recopilando, generando, gestionando, etc datos.
Esos datos los vamos persistiendo en bases de datos, que pueden ser de distintos tipos:
- Relacionales (SQL Server, MySQL, PostgreSQL, Oracle, etc)
- NoSQL
  No SQL no significa que no usen SQL. De hecho en inglés "no" se dice "not".
  Ese No de NoSQL son siglas: Not Only SQL 
    - Orientadas a objetos (MongoDB, CosmosDB, etc)
    - Orientadas a grafos (Neo4j, etc)
    - Jerárquicas (Cassandra, etc)
    - Clave-Valor (Redis, etc)

Los datos que tenemos en esos entornos no nos interesa tenerlos ahí de por vida, ya que:
- Si las BBDD crecen mucho, el rendimiento de las aplicaciones se ve afectado.
- El almacenamiento en los entornos de producción suele ser más caro.
- Teniendo más datos, es más complejo para un usuario identificar los datos que le interesan.

Una vez los datos mueren (ya no precisan de gestión) ya no son necesarios en producción, podemos moverlos a otros entornos. Esto lo puedo hacer por varios motivos:
- Requerimientos legales (por ejemplo, guardar facturas 5 años)
- O simplemente por interés.. Yo que se.. quizás el día de mañana quiero analizar esos datos para sacar conclusiones de negocio.


## ETLs

Para mover los datos creamos ETLs (Extract, Transform, Load). Esto son simples SCRIPTs que hacen:
- Extraen los datos de las BBDD de producción
- Los transforman (por ejemplo, eliminando datos que no me interesan, o agrupándolos)
- Y los cargan en otros entornos (DataLakes, DataWarehouses, etc)
Hay muchas variantes de ETLs:
- ETL: Extraigo de un origen, transformo y cargo en destino.
- ELT: Extraigo de un origen, cargo en destino y luego transformo.  
- TEL: Transformo datos en origen, los extraigo y los cargo en destino.
- TELT: Transformo datos en origen, los extraigo, los cargo en destino y luego los transformo más.
- TETL: Transformo datos en origen, los extraigo, los transformo más, y los cargo en destino.
En general a todos estos procesos los llamamos ETLs.

Estas ETLs las podemos desarrollar:
- Programando a pelo (Python, C#, Java, etc)
  Incluso hay frameworks que nos ayudan a ello desde distintos lenguajes: JAVA Spring Batch, .NET SSIS, Python AirFlow, etc
- Usando herramientas específicas de ETL: Azure Data Factory, Talend, Informatica Power, NiFi, etc

## Datalake

Al sacar los datos de un entorno de producción, en general queremos poca transformación. No sé para qué voy a usar esos datos. Solo sé que no los quiero en el entorno de producción.
Intento hacer una copia lo más fideligna posible de esos datos en otro entorno: DataLake

Un datalake es un almacen de datos en crudo, donde voy acumulando datos que ya no quiero en producción.... de muchas fuentes distintas. El datalake puedo crearlo de distintas formas... aunque lo más habitual es usar almacenamiento basado en ficheros (parquet ~ csv pero binary y con esquema).

    BBDD --> ETL --> Datalake

Transformaciones en este punto... pocas. Quizás un campo del tipo ESTADO de gestión... Coño pues si ya no lo estoy gestionando para qué quiero ese campo? Pues lo elimino.

## Business Intelligence

En ocasiones voy a usar esos datos para hacer análisis SIMPLONES que nos puedan aportar algo de luz acerca de cómo funciona nuestro negocio.

Básicamente, BI es aplicar técnicas de estadística descriptiva nivel instituto (a veces un poco más.. con series temporales, etc) para entender qué está pasando en el negocio y aportar INFORMACION que ayude a la toma de decisiones.

Es decir... Si conozco que en Diciembre del año 2020 he vendido muchas bufandas y poca gafas de sol, y en 2021 lo mismo y en 2022 también... y así hasta el 2024... Es posible que en Diciembre de 2025 también venda muchas bufandas y pocas gafas de sol.

Intentamos buscar relaciones entre variables que nos ayuden a entender el negocio. Habitualmente hay una información que quiero "adivinar", "predecir" o "explicar" (variable dependiente) y otras datos que me ayudan a ello (variables independientes).

Para hacer BI, que son puera puritas consultas cobre datos, no me interesa que los datos se guardeen como se guardan (misma estructura) en los entornos de producción. En ellos, los datos se guardan de forma que se optimice la gestión de los mismos por parte de las aplicaciones. (que sea fácil darlos de alta, baja, modificar, etc)

Es habitual usar modelos de datos muy estandarizados para sobre ellos montar cuadros de mando BI: Modelos en estrella, copo de nieve, etc.

    BBDD --> ETL --> Datalake --> ETL --> DataWarehouse <-- BI

En BI solemos juntar 2 variables... hasta 3. Más imposible. Nuestro limitado cerebro humano es totalmente incapaz de entender relaciones entre más de 3 variables.

## DataWarehouse - Almacén de Datos

Es otro almacén de datos, pero en este caso los datos ya están transformados y organizados facilitar ciertas técnicas de análisis (principalmente BI) sobre ellos.

Quizás el Datawarehouse lo monto sobre una BBDD relacional (SQL Server, Oracle, etc)

## Data Mining - Minería de Datos

En ciertos casos, puede ser que las técnicas de BI no sean suficientes para llegar a exprimir todo el potencial de los datos que tengo. Para conseguir hacer análisis más complejos, necesito usar técnicas de Data Mining.

Hacer programas de DataMining es muy simple. Básicamente no tenemos ni puñetera idea de cómo buscar cosas allí entre tanto dato.. y lo único que hacemos es un programa cutre que le dice al oprdenador... porfa porfa porfaa... búscame patrones en estos datos que yo soy incapaz.

Aquí ya buscamos relaciones entre muchas variables. 10, 20, 50, 100... lo que haga falta. Dale tiempo a la máquina!


    BBDD --> ETL --> Datalake --> ETL --> DataWarehouse <-- BI
                              --> ETL --> DataWarehouse 2 <-- DataMining / ML / DL / AI

## ML - Machine Learning

Básicamente tratar de predecir datos basándonos en otros datos históricos.
Báicamente lo mismo que Business Intelligence, pero usando técnicas más complejas (DataMining) para buscar relaciones entre muchas más variables.

Aquí es un poco más de lo mismo que DataMining. Hacemos programas que piden a la máquina que genere programas que sean capaces de predecir datos basándose en otros datos históricos, ya que nosotros no somos capaces de hacerlo.

Le damos al computador alguna pista de qué es lo que queremos predecir, y de cómo puede plantear el problema.

Aquí salen modelos de regresión, clasificación, clustering, etc. Técnicas:
- Arboles de decisión
  - Random Forest
- KMeans
- Redes Neuronales sencillas

## Deep Learning - Aprendizaje Profundo

Aquí montamos redes neuronales más complejas, con muchas capas, que son capaces de aprender representaciones de los datos a distintos niveles de abstracción.

La complejidad de una red neuronal se mide en:
- Número de capas
- Número de neuronas por capa
Otros factores:
- Tipo de capas (convolucionales, recurrentes, etc)
- Funciones de activación

Este mundo deja de usar CPUs. La cantidad de cálculos que hay que hacer es tan bestia, que ni muchísisisismas CPUs darían a basto. 
Aquí usábamos GPUs (unidades de procesamiento gráfico) que son capaces de hacer muchos cálculos en paralelo...
y hoy en día usamos TPUs (unidades de procesamiento tensorial) que son procesadores específicos para hacer cálculos de tensores (matrices multidimensionales) que es lo que se usa en Deep Learning.

Al final, una CPU o una GPU o una TPU no es sino un chip integrado con un huevón de transistores que hacen cálculos lógicos y matemáticos. Miles de millones de ellos.
Y depende de cómo conecte esos transistores entre sí, consigo que el chip sea más eficiente haciendo unos cálculos u otros.

En las CPUs hay más transistores conectados en serie, para hacer cálculos complejos de forma secuencial.
Una cpu de hoy en día puede tener 8 cores, 16 cores, 32 cores... 96 cores... cada core es capaz de hacer un cálculo con mucha precisión.

> Cómo calcula una computadora una raíz cuadrada, logaritmo, potencia? Mediente desarrollos de series de Taylor, aproximaciones sucesivas, etc. Es decir, haciendo muchos cálculos sencillos (sumas, restas, multiplicaciones, divisiones) para conseguir un resultado complejo.

Cuantos más términos coja de la serie, más preciso será el resultado. Pero más cálculos tendré que hacer.

Las CPUs son especialistas en calcular resultados complejos con mucha precisión. Dedican los transistores a calcular muchos términos de la serie para conseguir mucha precisión en cada cálculo.

Por contra, en una GPU o TPU, los transistores están conectados en paralelo. Puedo hacer muchísimos cálculos sencillos a la vez, pero con poca precisión.

No uso tantos transistores para calcular muchos términos de la serie, sino que uso pocos términos, pero hago muchísimos cálculos a la vez.

En una GPU puedo tener miles o decenas de miles de núcleos (cores), cada uno haciendo cálculos sencillos con poca precisión.

## AI - Artificial Intelligence

En general es cualquier programa que hace cosas que normalmente requieren inteligencia humana, o que simulan cierta inteligencia humana.

Y esos programas los podemos montar de 2 formas distintas:
- Usando reglas definidas por humanos (Sistemas Expertos) (Cientos de IF... THEN... metidos en el códigoa fuego)
- Dejando a la computadora que aprenda de los datos (Machine Learning / Deep Learning)

Estos programas, sobre todo los segundos, los usamos para:
- Predecir datos
- Clasificar datos
- Generar datos nuevos (imágenes, texto, audio, video, etc)
  - LLM

En general cuando hablamos de IA hoy en día, nos referimos a mnodelos basados en Deep Learning (Redes neuronales profundas).

---

## BigData

Muchas veces pensamos que BigData tiene que ver con grandes volúmenes de datos... o con analizar datos ... pero es tanto eso.

BigData tiene que ver con la forma en que procedo a resolver cierto tipo de problemas al trabajar con datos.
NOTA: Cualquiera que sea el trabajo que voy a realizar con el dato:
- Almacenar datos
- Procesar datos
- Analizar datos
- Transmitir datos

En ocasiones las técnicas que hemos venido aplicando para reolver o enfreentarnos a estos problemas ya no me son eficientes o válidas. Esto puede pasar debido a muchos factores:
- El volumen de datos ha crecido tanto que las técnicas tradicionales no son eficientes.
- Se generen datos a una velocidad tan alta que las técnicas tradicionales no son capaces de procesarlos en tiempo y forma.
- Los datos sean tan complejos (estructurados, semiestructurados, no estructurados) que las técnicas tradicionales no son capaces de gestionarlos.
- La ventana de disponibilidad (de vida últi) del dato sea tan corta que las técnicas tradicionales no sean capaces de gestionarlos.

No hay una linea que dice, hasta aquí usas técnicas tradicionales, y a partir de aquí usas técnicas BigData.

> Tengo un USB de 16Gbs limpito que acabo de sacar de la caja. Quiero guardar un archivo de 5 Gbs en él. Puedo? Depende del formato. 
Fat16 solo me permite archivos de hasta 2Gbs. Fat 32 hasta 4Gbs. 
Incluso otros formatos tienen sus límites. NTFS no tiene límite práctico.... pero tengo otro problema.. Cuántos HDD soy capaz de meter bajo control de un SO para formar un espacio de almacenamiento de 10Pb o 10Eb?

Y qué hago si tengo un fichero de 1 Pb? Dónde lo guardo? cómo lo guardo? Con que sistema de ficheros lo hago?

> Quiero hacer la lista de la compra:
- Bloc de notas... si tengo menos de 1000 cosas que comprar
- Excel... si tengo entre 1.000 y 100.000 de cosas que comprar
- MySQL... si tengo entre 100.000 y 10.000.000 de cosas que comprar
- SQL Server... si tengo entre 10.000.000 y 100.000.000 de cosas que comprar
- Oracle... si tengo más de 100.000.000 de cosas que comprar... hasta 10.000.000.000 empieza a llorar

y entonces qué?

> Juego en linea. Clash Royale 2vs2.

En un segundo hacias 2 movimientos.Eso significa que el última instancia cada movimiento que hago tiene que ser notificado a 3 jugadores (mi compañero, y los 2 rivales).
1 movimiento -> 3 mensajes que hay que entregar... para que el juego sea jugable la latencia máxima es de 500ms.
Si en un segundo hago 2 movimientos... tengo que enviar 6 mensajes en 1 segundo... y asegurarme que llegan en menos de 500ms.
Pero somos 4 jugando: 4 jugadores x 6 mensajes = 24 mensajes por segundo... y eso solo en 1 partida.
si en un momento hay 50k partidas en curso... 50.000 x 24 = 1.200.000 mensajes por segundo.

No hay servidor en el mundo capaz de gestionar esa carga de trabajo.

En estos escenarios puedo optar por un enfoque bigdata:
BigData implica una determina infraestructura y un determinado software junto con ciertas técnicas de desarrollo para enfrentarme a este tipo de problemas. Básicamente se trata de usar una granja de ordenadores de mierda (commodity hardware) y usar la potencia combinada de todos ellos para resolver el problema... haciéndoles trabajar como un solo ordenador gigante.

Esto es un follón! Gestionar una granja de miles de ordenadores es un follón. Comprarlos... ya es un follón... ubicarlos en el cpd otro follón... alimentarlos de energía otro follón... refrigerarlos otro follón... conectarlos en red otro follón... instalarles un sistema operativo otro follón... mantenerlos actualizados otro follón... monitorizarlos otro follón... programar aplicaciones que funcionen en esa granja otro follón...

La primera cosa que tendríamos que hacer si nos piden trabajar en un proyecto BigData es SALIR CORRIEENDO... cuesta abajo sin frenos!!! Ni mirar atrás! Si puedo evitar meterme en este follón lo evitaré a toda costa.

Lo que pasa es que a veces no me queda más remedio que meterme en el follón. Otras veces es que aún teniendo alternativas, me sale más barato meterme en el follón.

De hecho, la mayoría de los proyectos (que usan ténicas/Estrategías) BigData que se hacen hoy en día podrían resolverse perfectamente con técnicas tradicionales... pero sale más barato uisar enfoques bigdata.

Es decir... para saturar uno de esos megaservidores de Oracle... hace falta mucha mucha mucha carga de trabajo.
No hay tantos clientes, que necesite usar estas técnicas... y de esos clientes, cada uno tendrá muy pocos proyectos donde sea necesario.

Movistar. Para generar las facturas mensuales de todos mis clientes necesito técnias bigdata? 10 Millones- 50 Millones de clientes. 200 millones de facturas al mes? Eso es calderilla!
Movistar tendrá algunos casitos donde necesite aplciar técnicas bigdata... pero serán casos muy concretos y muy pocos.

Y pocas empresas hay de ese volumen.

### Por qué está tan de moda?

La realidad es que la mayor parte de los proyectos donde aplicamos técnicas bigdata, podrían resolverse con técnicas tradicionales... lo que pasa es que sale más caro.

Imaginad que tengo que montar una ETL... Esa ETL tiene que sacar datos de una BBDD, Transformarlos y cargarlos en otro sitio. Ese programa moverá al día (1 hora - 02:00-03:00am) unos 500 Gbs de datos.... más o menos (habrá días que más... habrá días que menos). Necesito aplicar téecnicas bigdata para hacer esa ETL? NO... Con Java Spring Batch o con SSIS de SQL Server lo hago sin problemas.

Entonces, por qué usar técnicas bigdata? Y la realidad es que en ese tipo de proyectos cada vez se usan más técnicas bigdata.

Ese programa va a funcionar 1 hora... Puedo comprar un servidor que me cueste lo que sea y en esa hora sea capaz de mover esos 500 Gbs sin problemas... pero ... y que pasan las 23 horas restantes del día? El servidor cogiendo polvo? Muy caro! Qué pasa si un día llegan 900 Gbs? Y el servidor no me da de si. Qué pasa si un día llegan 100 Gbs? Y acabo en 10 minutos.. sin necesidad... y los otro 50min + 23 horas... el servidor cogiendo polvo?

El problema se llama ESCALABILIDAD. Capacidad de ajustar la infraestructura a la carga de trabajo que tengo en cada momento.
Hoy en día quiero flexibilidad. Me la juego comprando un servidor muy caro, y que dentro de 6 meses se me quede pequeño... o grande. O que solo necesite trabajo de ese servidor pequeños momentos del día. O que puntualmente a lo largo del año en 3 o 4 ocasiones necesite más potencia.

En estos casos, una gran ventaja de las técnicas bigdata es que esa granja de ordenadores de mierda (commodity hardware) puedo irle poniendo más o menos ordenadores bajo demanda, según la carga de trabajo que tenga en cada momento. Y ESO SIN NECESIDAD DE CAMBIAR NADA EN EL SOFTWARE QUE HE DESARROLLADO. Haré programas que funcionen en esa granja o en cualquier otra. Que necesiten de una granja...Y que se puedan adaptar al tamaño de granja que tenga en cada momento. <-- GUAY!

Este es el motivo principal por el que las técnicas bigdata están tan de moda hoy en día.

Claro... llamar al tio de Dell para que a las 2:00 me traiga 3 servidores nuevos para que los meta en la granja... y que se los lleve a las 03:00 que ya no los necesito... no puedo hacerlo. Y Aquñi es donde estan los CLOUDs, como complemento perfecto a las técnicas/infraestructuras bigdata.

## Cloud

Un cloud es el conjunto de SERVICIOS (relacionados con el mundo de la TIC) que una empresa ofrece a traves de internet, mediante un modelo de pago por uso.

IBM antes vendía muchas máquinas. Hoy en día sigue vendiendo.. pero muchas menos.
Hoy en día ha creado un cloud... IBM Cloud, que recoje servicios que ofrece a sus clientes, y que estos consumen por internet, pagando por uso.
Lo mismo hace Microsoft con Azure, Amazon con AWS, Google con GCP, Oracle con Oracle Cloud, y cientos más.

Esos servicios pueden ser de 3 tipos fundamentales:
- IaaS - Infraestructura como Servicio
         Alquiler de máquinas virtuales, almacenamiento, redes, etc
- PaaS - Plataforma como Servicio
         Alquiler de BBDD, Servicio que me permita desarrollar IAs, ETLs, ...
- SaaS - Software como Servicio
         Alquiler de aplicaciones completas pensadas para usuario final (Office365, Gmail, Salesforce, etc)

- Databricks ( lo encontramos en AWS, Azure y IBM Cloud)
- Datafactory (Azure)
- Synapse Analytics (Azure)
- HDInsight (Azure)
- IA Forge (Azure)

Normalmente las soluciones de tipo BigData se montan sobre infraestructuras Cloud, ya que estas me permiten escalar la infraestructura de forma rápida y sencilla, pagando solo por lo que uso en cada momento.

---

# BigData

## Cómo empieza este mundillo?

Esto arranca con una gran empresa que en su momento no lo era tanto... pero que fué la primera en tener realmente problemas de volumenes de datos muy grandes... Google.
Estaban scrapeando la web para montar su motor de búsqueda... y los datos que tenían que gestionar eran bestiales.

Al principio usaron MySQL para gestionar esos datos... pero pronto se dieron cuenta que no les servía.

Montaron su propia BBDD: Google BigTable

Para montar esa BBDD, usaron 2 tecnologías que habían desarrollado internamente:
- Un sistema de archivos distribuido: Google File System (GFS)
  Permitía trocear un archivo en framentos y repartir esos fragmentos entre muchos servidores.
  De esta forma un archivo se guardaba no en un solo servidor, sino que se repartía entre muchos servidores.
  De hecho cada fragmento se guardaba no solo en un servidor, sino que se replicaba en varios servidores para asegurar la disponibilidad.
  Esto daba un ancho de banda de lectura y escritura bestial, ya que podía leer el archivo desde 50 servidores a la vez x50 del ancho de banda. En escritura los mismo.
- Una teoria (junto con un programa, una implementación) para crear programas (algoritmos) que funcionaran aprovechando la capacidad conjunta de cómputo de muchos servidores: Modelo de programación MapReduce. Esto es un modelo teórico, que además google implementó dentro de su bbdd BigTable.

Eran cosas nuevas... y eran otros tiempos... Y google las compartió ... más o menos. No sus herramientas, pero si sus ideas... en unos papers que publicó.

Basándose en el diseño de esos papers, un desarrollador creo su propia implementación open source de un sistema de archivos distribuido y del modelo de programación MapReduce. A ese software le llamó Hadoop (en honor al elefante de peluche de su hija). Ese proyecto se donó a la fundación Apache, y hoy en día es uno de los proyectos más grandes y activos de Apache.

Hadoop tiene/ofrece 3 cosas:
- HDFS - Hadoop Distributed File System
  Un sistema de archivos distribuido basado en GFS de google.
- YARN - Yet Another Resource Negotiator
  Un programa encargado de monitorizar y gestionar los recursos (cpu, memoria, red, disco) de la granja de ordenadores.
- Una implementación del modelo de programación MapReduce, que es un puñetero desastre.
  Digo desastre ya que funciona, pero cada nodo de la granja, lo primero que hace cuando recibe una tarea es escribir los datos en disco... y al terminar la tarea vuelve a escribirlos a disco antes de enviarlos al nodo que los necesita.
  Eso mete una latencia bestial en los procesos.

Hadoop viene a ser el equivalente a un SO para una granja de ordenadores.
Me permite llevar una carga de trabajo a esa granja, y que la granja la ejecute repartiendo la carga entre todos los nodos que la forman.

Habitualmente un SO usa el HW de una computadora para llevar a cabo un trabajo.
- Los cores de ese nodo para hacer cálculos
- La memoria RAM para guardar datos temporales
- El disco para guardar datos persistentes
Gestiona todos esos recursos para que las aplicaciones que corren en ese nodo puedan hacer su trabajo.

Eso mismo es lo que hace Hadoop, pero a nivel de granja de ordenadores.
Hadoop usa el HW de una granja de computadoras para llevar a cabo un trabajo.
- Los cores de toda esa granja para hacer cálculos
- La memoria RAM de todos los nodos para guardar datos temporales
- El disco de todos ellos para guardar datos persistentes
Gestiona todos esos recursos para que las aplicaciones que corren en esa granja puedan hacer su trabajo.

Reparte las tareas (procesos) entre los cores disponibles (no de la computadora) en la granja.
Asigna memoria RAM a los procesos que se ejecutan (no de la computadora) en la granja.
Gestiona el almacenamiento en disco (no de la computadora) de la granja.

En este sentido, es en el que Hadoop es un SO para una granja de ordenadores.

Pero igual que nos pasa con los SO tradicionales, Por si solos no aportan mucho valor.

Yo puedo instalar Windows en mi PC... y ahora que? Tengo Windows...
- Puedo crear carpetas
- Puedo crear usuarios
- Incluso jugar al buscaminas! GUAY!
- Pero valor, valor... lo que viene a ser valor... aporta poco.

Claro... los que aportan son los programas que pongo encima de Windows:
- Word
- Excel
- VSCode
- Chrome
- Photoshop

Hay toda una generación de programas que se han desarrollado para correr sobre una granja de ordenadores gestionada por Hadoop... programas que guardan relación con el DATO!
- BBDD:
   - HBase (inspirada en BigTable de google)
   - Hive (BBDD SQL sobre HDFS)
   - Cassandra (NoSQL distribuida)
- Procesamiento de datos:
   - Pig (Lenguaje de procesamiento de datos sobre Hadoop)
   - Spark (Procesamiento de datos en memoria sobre Hadoop)
   - Storm (Procesamiento de datos en tiempo real sobre Hadoop)
- Analítica:
   - Mahout (Librerías de Machine Learning sobre Hadoop)
   - Oozie (Orquestador de trabajos sobre Hadoop)
- Sistemas de mensajería:
   - Kafka (Sistema de mensajería distribuido)
   - Flume (Recolección y transporte de grandes volúmenes de datos)

Esos programas son los que aportan valor a negocio. Y esos programas se montan sobre una granja de ordenadores gestionada por Hadoop ( a su vez, ordenadores con Linux, como SO base a bajo nivel en cada host)...
Espera... HAs dicho LINUX??? y AZURE???? Microsoft!!!??!?!?!?! Mi cabeza explota!
Le mola a Microsoft Linux? Lo adora. Y .. que pasa con Windows?
Microsoft ha entendido el lugar de su familia de SO.
Y ha aceptado que en el mundo de los servidores, la apuesta es Linux.
De hecho ha entendido que incluso en el mundo PC linux es importante. Y por ello, desde hace varias versiones de Windows, hoy en día es posible (de forma nativa... sin instalar cosas raras) ejecutar un kernel Linux en paralelo con el Kernel de Windows (NT=New Tecnology). Esto lo da microsoft... solo hay que entra en características de windows y activar el subsistema de windows para linux (WSL).

Hablar de BigData es hablar de:
- Una granja de ordenadores (commodity hardware), normalmente, aunque no necesariamente, en un cloud
- Un SO para esa granja (Hadoop u otros)
- Programas que corren sobre esa granja gestionada por ese SO, y que trabajan con datos (BBDD, Procesamiento, Analítica, Mensajería, etc)
- Un sistema de archivos distribuido (HDFS u otros)
- Un modelo de programación distribuida (MapReduce u otros)

Y eso lo aplico a problemas de:
- Almacenamiento de grandes volúmenes de datos
- Procesamiento de grandes volúmenes de datos (ETLs)
- Análisis de grandes volúmenes de datos (BI, DataMining, ML, DL, AI)
- Transmisión de grandes volúmenes de datos (Mensajería, IoT, etc)

Decía un compañero cuando nos hemos presentado...
- Yo me he dedicado al mundo del Machine learning y data mining tradicional.

En concreto, decía que la implementación del modelo MapReduce de Hadoop era un desastre. Hay un proyecto (otro de la fundación Apache) que ofrece otra implementración MUCHO más eficiente de un modelo de programación MapReduce: Apache Spark. Esa implementación trabaja en RAM, en lugar de en disco... y eso mejora mucho el rendimiento.

De hecho muchos de los programas que corren sobre Hadoop, hoy en día usan Spark en lugar del MapReduce de Hadoop.

Spark es otro proyecto de Apache. Lo cierto es que Spark es más que una reimplementación del modelo de programación MapReduce. En concreto eso, es lo que se llama Spark Core.
Pero Spark tiene otras librerías que aportan más funcionalidades:
- Spark SQL: Permite hacer consultas SQL sobre datos en Spark
    ^^^
- Spark Streaming: Permite procesar flujos de datos en tiempo real
- MLlib: Librerías de Machine Learning sobre Spark
- GraphX: Librerías para trabajar con grafos sobre Spark

Microsoft, en su cloud Azure, ofrece muchos servicios relacionados con BigData:
- Azure HDInsight: Servicio gestionado de Hadoop y Spark
- Azure Databricks: Servicio gestionado de Apache Spark
- Azure Synapse: Todo en uno... Es básicamente la evolución del SSIS/SSAS/SSRS de SQL Server, pero en la nube y con muchas funcionalidades BigData integradas (Spark, DataLake, DataWarehouse, etc)
- Datafactory: Servicio de ETLs en la nube (opcionalmente con capacidades BigData)
- Y más, que veremos estos días.


Databricks es algo así como la versión de pago de Apache Spark. Lo hacen los creadores de Spark, pero lo han reescrito entero en lenguaje C++ para mejorar el rendimiento (mientras que Spark corre sobre JVM). Además le han añadido muchas funcionalidades extra para facilitar el desarrollo de aplicaciones de BigData e ML (IAs).
Es un producto independiente de Azure, que también está disponible en AWS y en IBM Cloud.
Aunque la integración con Azure es muy buena.

---


# Azure: BigData e IA

---

# Nota 1: Es el almacenamiento hoy en día barato o caro?

Hoy en día el almacenamiento es lo más caro que hay en un entorno de producción.

Podemos pensar que hoy en día comprar un HDD o un SSD es barato... y comparado con 50 años atrás lo es!

Para casa compro un HDD Western blue de 2TB por menos de 50-70 euros. Disco de muy baja calidad. Me sirve para guardar archivos 3 veces al mes y consultarlos 1 al mes. Y usándolo así me dura años.

En una empresa, un hdd se usa de forma diferente.. mucho más intensiva... 24x7
Además, el ancho de banda que se necesita es mucho mayor.

nvme red pro 2 tbs son 200€... Para casa... para juegos... para que el juego de turno me cargue en 2 segundos en vez de 5.
Un disco como ese tiene una velocidad de lectura/escritura de 3500 MB/s
Pero en casa tengo una red de 1 Gbps... que son 125 MB/s.

Un servidor en una empresa tiene no una tarjeta de red.. puede tener fácil 8-20 tarjetas de red de 10-20-40 Gbps cada una.

Oracle vende para sus servidores T8-Exadata un nvme de 2Tbs por unos 3500€... estamos multiplicando por 17 el precio de un nvme normal.

Pero eso es la punta del pastel.

En un entorno de producción, los datos se guardan al menos en 3 sitios diferentes. Dicho de otra forma, para conseguir esos 2Tbs, en un entorno de producción necesito comprar 3x2Tbs... es decir que esos 3500€ se convierten en 10.500€.
Y eso es para conseguir Alta Disponibilidad. Otro concepto es el de recuperación ante desastres. Para eso necesito tener backups de hasta hace 2 semanas. Eso significa que necesito muchos más discos. De esas copias, tendré redundancia (x2)
y evidentemente las haré en discos más baratos (rotacionales, HDD), pero aun así sigue sumando.

Al final, esos 2 Tbs que en casa me cuestan 200€, en un entorno de producción me pueden costar fácilmente 20-25.000€.
Estamos multiplicando el precio por 100x.

---

# Nota 2: Dato vs Información

Dato es una medida bruta que tengo. En bruto, sin procesar. Me informa de una cualidad o cantidad de una propiedad de un sujeto de estudio.

Felipe pesa 50kgs
Federico pesa 150Kgs

Otra cosa es la información que ese dato transporta, que va mucho más allá del dato en sí.
Que Federico pese 150 Kgs no me informa solo del peso de Federico. Me informa de muchas otras cosas:
- El estado de salud de Federico
- De su talla de ropa No será nunca inferior a 3XL
- De su estilo de vida
- De su nivel de triglicéridos

A más datos que tenga, más precisa será la información que pueda extraer de ellos, y menor probabilidad de error tendré en mis conclusiones.