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