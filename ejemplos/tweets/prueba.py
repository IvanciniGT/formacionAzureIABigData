# Importar las libreas necesarias
from pyspark import SparkContext, SparkConf

# PASO 1: Crear la configuración de Spark
# SparkConf me permite establecer la configuración de mi aplicación Spark:
# - Nombre de la aplicación
# - Dar la ruta del cluster contra el que me quiero conectar (ESTO REALMENTE LUEGO NO LO HACEMOS ASI)
conf = SparkConf().setAppName("Mi primera aplicación Spark").setMaster("local[2]")
# Habitualmente la ruta (RUL) de un cluster de spark es del tipo: spark://ip_del_nodo_master:puerto(7077 por defecto)
# En mi caso, como aún no tengo un cluster real de Spark, voy a usar "local"
# local hace que se levante un cluster en mi máquina para desarrollo y pruebas. 
# Ese cluster solo se ejecuta mientras mi app se está ejecutando
# Una cosa adicional aquí es el [*]
# Dentro de los corchetes indicamos el número de cores máximos que puede usar Spark en mi máquina local
# El * indica que use todos los cores disponibles en mi máquina: COSA QUE NUNCA HAGO.
# Me deja la máquina frita! Solo quiero hacer pruebas!

# Ahora creo el contexto de Spark: La conexión entre mi aplicación y el cluster de Spark
sc = SparkContext(conf=conf)

# PASO 2: Preparo los datos
listado = [1,3,5,7]
# A través de la conexión, paralelizo los datos para su procesamiento. 
# Básicamente estoy mandando los datos al cluster de Spark
rdd = sc.parallelize(listado, 2) # Esta función devuelve un tipo de dato llamado RDD (Resilient Distributed Dataset)
# Sobre un rdd es obre el tipo de objeto que puedo aplicar operaciones de tipo map reduce

# Y aquí encajamos con algo que comenté ayer:
# Una operación de tipo map es una operación que al aplicarla sobre una colección de datos que soporta programación map/reduce devuelve otra colección de datos 
# que también soporta programación map/reduce
# En Spark, una operación de tipo map es una operación que al aplicarse sobre un RDD devuelve otro RDD.
# En Spark, una operación de tipo reduce es una operación que al aplicarse sobre un RDD devuelve lo que sea que no sea un RDD.

# PASO 3: Algoritmo MapReduce
def doblar(numero):
    return numero * 2

def dividir_entre_3(numero):
    return numero / 3

def redondear(numero):
    return round(numero)

def sumar_5(numero):
    return numero + 5

def es_par(numero):
    return numero % 2 == 0

resultado = rdd.map(doblar) \
   .map(dividir_entre_3) \
   .map(redondear) \
   .map(sumar_5) \
   .filter(es_par) \
   .collect() # collect() es una operación de tipo reduce que me devuelve los datos al programa principal

# PASO 4: HAgo lo que tenga que hacer con el resultado
print("El resultado final es:", resultado)

# PASO 5: Cierro la conexión con el cluster de Spark
sc.stop()