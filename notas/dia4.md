# Lo que llevamos:

- Establecer cierto vocabulario básico:
   - BBDD en un entorno productivo
   - DataLake
   - DataWarehouse
   - ETLs
   - Business Intelligence
   - Data Mining
   - Machine Learning
     - Deep Learning (Redes neuronales complejas)
   - Bigdata
- Establecer el concepto de programación funcional.
- Intro al concepto de BigData
  - Usar una granja de commodity hardware para hacer operaciones 
    - con grandes volúmenes de datos
    - o datos que cambian /se generan muy rápido
    - datos muy complejos
    - cuando necesitamos escalabilidad horizontal (bien por volumen de trabajo, bien para ahorrar costes)
  - Google es quién arranca con esto: BigTable:
    - GFS
    - Programación MapReduce
  - Hadoop como implementación open source de estas ideas
    - HDFS
    - YARN
    - MapReduce
  - Distintas herramientas que se han desarrollado alrededor de Hadoop:
    - Hive
    - Pig
    - HBase
    - Spark
    - ...
  - Spark: Ofrece una implementación alternativa al MapReduce de hadoop
    - Hicimos ejemplos de MapReduce: Tweets
- Intro más produnda al concepto de DeepLearning:
  - Como son las Redes neuronales
  - Que significan esas neuronas o perceptrones
  - Arquitecturas de redes neuronales
    - Número de capas
    - Cantidad de perceptrones por capa
    - Funciones de activación
  - Uso actual de todo esto.
    - Partimos dee trozos de red neuronal ya entrenados (Modelos preentrenados)
    - Librerías como HuggingFace

---

# Próximos pasos

- Lunes: Bigdata:
  - Intro a Azure
  - Configurar las cuentas.
    - Descargar Microsoft Authenticator en el móvil
  - Almacenamiento: Cuenta de almacenamiento
    - DataLake Gen2. Almacenamiento de ficheros para Bigdata ~ Es algo asi como la implementación de Azure de HDFS.
  - Procesamiento: Azure Databricks ~ Es una implementación de clase empresarial de Spark. Adeemás de eso, nos ofrece un entornos completo para trabajar con Bigdata.
  - DataFactory ~ Servicio de orquestación de procesos ETL/ELT -> Definir flujos de trabajo que tengamos en Databricks y otros servicios.
- Martes:
    - Terminaremos con DataFactory
    - Synapse
    - Otros.

- Miércoles: IA: IA Studio de Azure <-- muy sencilla de manejar, muy potente, pero limitada en cuanto a personalización.
- Jueves:        Forge de Azure     <-- más compleja de manejar, más potente, y mucho más personalizable.

---

# Azure

Es el cloud (es decir, el conjunto de servicios) que ofrece Microsoft relacionados con el mundo IT y accesibles desde internet con un modelo de pago por uso.

Tenemos servicios de muchos tipos:
- IaaS: Infraestructura como servicio
  - Máquinas virtuales
  - Redes virtuales
  - Almacenamiento:
    - Ficheros
    - Bloques
    - Objetos (blobs)
- PaaS: Plataforma como servicio
  - Bases de datos gestionadas
  - Servicios de bigdata: Databricks, Synapse, DataFactory
  - Servicios de IA: IA Studio, Forge
- SaaS: Software como servicio
  - Office365
  - Dynamics365
  - Otros.

## Conceptos clave dentro de Azure:

- Resource Group: Es un contenedor lógico donde agrupamos recursos relacionados.
                  Nos simplifica la gestión de esos recursos:
                  - Eliminarlos de una
                  - Moverlos de un sitio a otro
                  - Controlar costes
                  - Compartirlos
- Región: Es la localización física donde se alojan los recursos: Europa, America del Norte, Asia...
          Cada región tiene varios centros de datos (data centers).
          Algunos servicios están disponibles en todas las regiones.
          Otros servicios sólo están disponibles en algunas regiones.
- Gestión de identidades. Microsoft tiene su propia herramienta/Servicio de gestión de identidades: Azure Entra ID (antes Azure AD)
  - Usuarios
  - Grupos
  - Roles
  - Políticas de acceso
  - Autenticación multifactor (MFA)
  - Aplicaciones registradas
  - Etc.

---

# Que incluye databricks:
- Gestión automática de clusters de Spark
- Entorno de desarrollo colaborativo basado en notebooks (Jupyter like)
- Es una BBDD distribuida optimizada para bigdata (Delta Lake) (esta basada en Apache Hive. Trabaja con archivos similares (basados en Parquet) pero optimizados )
- Además tiene una parte llamada MLflow para gestionar el ciclo de vida de los modelos de machine learning.
  - La realidad es que esta parte la usamos poco.

---
Spark como framework ofrece varias librerias:
- Spark core: Es la que ofrece la programación map-reduce distribuida.
- Spark SQL: Permite trabajar con datos estructurados usando SQL.
- ~~Spark Streaming: Permite procesar flujos de datos en tiempo real.~~Hoy en día su funcionalidad se ha movido a SparkSQL
- MLlib: Librería de machine learning distribuido. Tiene muy pocos modelos... y a pesar de estar trabajando contra un cluster, la cantidad de operaciones que hace es baja (usa cores de CPU pero no GPU) --> IA Forge, IA Studio
---

# Jupyter 

Es un entorno de desarrollo badado en el concepto de Notebook.
Antiguamente se llamaba Jupyter notebook, ahora es JupyterLab.

Esos notebooks son documentos que pueden contener:
- Código ejecutable en distintos lenguajes (Python, R, Julia, Scala...)
- Documentación en markdown

Esos notebooks los ejecutamos (su código) en un kernel.

## Kernel?

El kernel es el motor que ejecuta el código de un notebook.
Puede tener distintos kernels:
- IPython (Python)
- IRkernel (R)
- IScala (Scala)

En general, al trabajar con Jupyter, lo primero que necesitamos es elegir un kernel.
Eso me viene simplificado en entornos como Databricks, donde ya tengo el kernel de Spark listo para usar, con python.
Lo único que necesito es elegir el cluster de spark contra el que trabajo.


---
                          byte-code
.java ---> compilación ---> .class ---> JVM ---> ejecución
                           (interprete)
                                         ^
                                         JIT (Just In Time compiler. El que hace la interpretación)
                                         En java, en la versión 1.2 se añadió al JIT el HOT SPOT.
                                         Cache de compilaciones.

---

# Archivos parquet

Es un formato muy usado en el mundo bigdata.
Hay 2 formatos en bigdata: PARQUET y AVRO.

En el mundo bigdata no solemos usar formatos tipo:
 JSON
 XML
 CSV

Son una ruina enorme en el almacenamiento y lectura de los datos.
Son formatos de texto plano:
- Ocupan mucho espacio
- Necesito leerlos o escribirlos secuencialmente (enteros) para procesarlos.

Imaginad un número de DNI... que quiero tener guardado en un archivo.
- DNI = 99999999X
  - En un archivo de texto planso se guarda como una cadena de caracteres.
    Dependiendo del encoding, (UTF-8, ASCII, ISO-89859-1) ocuparía 1 byte por carácter.

Si el dato lo pudera guardar como NUMERO (BINARIO)
1 byte podría guardar hasta 256 números
2 bytes podrían guardar hasta 65.536 números
4 bytes podrían guardar hasta 4.294.967.296 números

Con 4 bytes me sobra para guardar el DNI como número. Luego si quiero guardo la letra aparte = 1 byte más.
TOTAL = 5 bytes en binario vs 9 bytes como texto. 

Como texto me ocupa casi el doble.

Eso me pasa con los números, las fechas, los booleanos...

AVRO y PARQUET son archivos BINARIOS.. y optimizan un huevo el almacenamiento de datos.
Y cuando tengo muchos datos, eso se nota.

Pero luego hay otra, y es la diferencia precisamente entre AVRO y PARQUET.

AVRO es un formato orientado a filas.
PARQUET es un formato orientado a columnas.

---
Si mirásemos internamente el binario, como se organiza por dentro, lo que veríamos en ambos casos es que esos ficheros comienzan con una cabecera, en la que se define el esqueman de datos (los nombres de las columnas, los tipos de datos, etc).

En el caso de parquet, después de la cabecera, Se guarda un índice de las columnas que hay en eel fichero, en que byte comienzan.
En el caso de avro, después de la cabecera, se guarda un índice de las filas que hay en el fichero, en que byte comienzan.
Luego van las filas o las columnas...

Algo asi:

---
CSV:
Nombre | Apellido | DNI | FechaNacimiento
Juan   | Pérez    | 12345678X | 1980-01-01
Ana    | Gómez    | 87654321Y | 1990-02-02
Luis   | Martínez | 11223344Z | 1975-03-03
---

En PARQUET (orientado a COLUMNAS):
---
Cabecera (esquema de datos)
Nombre: texto,         Byte en el que empieza (Linea 6)
Apellido: texto        Byte en el que empieza (Linea 7)
DNI: texto             Byte en el que empieza (Linea 8)
FechaNacimiento: fecha Byte en el que empieza (Linea 9)
Juan, Ana, Luis
Pérez, Gómez, Martínez
12345678X, 87654321Y, 11223344Z
1980-01-01, 1990-02-02, 1975-03-03
---
EN AVRO (orientado a FILAS):
---
Cabecera (esquema de datos)
NOMBRE: texto
APELLIDO: texto
DNI: texto
FECHANACIMIENTO: fecha
Registro1: Empieza en tal byte (Linea 9)
Registro2: Empieza en tal byte (Linea 10)
Registro3: Empieza en tal byte (Linea 11)
Juan, Pérez, 12345678X, 1980-01-01
Ana, Gómez, 87654321Y, 1990-02-02
Luis, Martínez, 11223344Z, 1975-03-03
---

En Spark por ejemplo, que aplicamos transformaciones columnares a los datos, es mucho más eficiente trabajar con archivos PARQUET que con AVRO.

Si dejamos datos en KAFKA, los datos luego son procesados fila a fila, es mejor AVRO.

  APPS --> TWEETS --> KAFKA (AVRO) --> SPARK --> PARQUET ---> DATA LAKE

Databricks extiende el formato PARQUET con su propio formato DELTA LAKE.

Tablas DELTA De Databricks son tablas basadas en archivos PARQUET, pero con metadatos extra que permiten asignar versiones a los datos, para luego poder viajar en el tiempo.
- Quiero ver los datos tal y como estaban el día 1 de junio a las 10:00 AM.
- Quiero compararlos con los datos tal y como estaban el día 15 de junio a las 10:00 AM.

---

En un escenario más reeal, leeríamos los datos de una herramieenta como Kafka.
Y kafka, cuando nos conectamos internamente gestiona offsets de lectura.
Y datos que ya ha sido leídos por un consumidor, no los vuelve a enviar.

Si estoy leyendo de ficheros de texto, lo normal es que :
 1. O elimine/mueva los ficheros que ya he procesado a otra ruta (si es que me interesa mantenerlos    )
 2. Generar un identificador único de cada fila (un hash por ejemplo).
 3. Lo que hacemos es asignar un timestamp a los datos cuando se leen por primera vez.


AVRO:
- TWEET     \
- USUARIO    > CONCAT de los datos y genero una huella digital (hash) SHA256
- FECHA     /

Esas tablas delta en el mundo databricks es lo que se conoce como un data lakehouse.
Es un híbrido entre un data lake y un data warehouse.
Donde tengo datos en bruto (data lake) y pero con cierto tratamiento que me sirve fácilmente para hacer análisis (data warehouse), por la forma en que están guardados (a nivel de columnas, y además con el control de versiones).

Es habitual a las tablas que vamos generando en un databricks, decir que las agrupamos en:
- Capa bronze: Datos en bruto, tal cual los he leído.
- Capa silver: Datos ya tratados, limpiados, con formatos adecuados.
- Capa gold: Datos ya preparados para análisis, con agregaciones, etc.