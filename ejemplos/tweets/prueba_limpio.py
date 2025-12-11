
from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("Mi primera aplicación Spark").setMaster("local[2]")
sc = SparkContext(conf=conf)
sc.setLogLevel("DEBUG")

listado = [1,3,5,7]

rdd = sc.parallelize(listado, len(listado)/200)

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

resultado = rdd \
   .map(doblar) \
   .map(dividir_entre_3) \
   .map(redondear) \
   .map( sumar_5 ) \
   .filter(es_par) \
   .collect()

    # rdd [1,3,5,7]
    # .map(doblar) -> rdd [2,6,10,14]
    # .map(dividir_entre_3) -> rdd [0.6666...,2,3.3333...,4.6666...]
    # .map(redondear) -> rdd [1,2,3,5]
    # .map(sumar_5) -> rdd [6,7,8,10]
    # .filter(es_par) -> rdd [6,8,10]


print("El resultado final (funciones clasicas) es:", resultado)

rdd = sc.parallelize(range(1, 1000000001))
## Reescribo usando lambdas:
resultado = rdd \
   .map( lambda numero: numero * 2 ) \
   .map( lambda numero: numero / 3 ) \
   .map( lambda numero: round(numero) ) \
   .map( lambda numero: numero + 5 ) \
   .filter( lambda numero: numero % 2 == 0 ) \
   .collect()

print("El resultado final (lambda) es:", resultado)

sc.stop()

print("Ahora con programación imperativa básica:")
# Hemos resuelto este problema con programación map/reduce
# Pero... podría haberlo resuelto con programación imperativa básica:

listado = list(range(1, 1000000001))  # Creo una lista con los números del 1 al 1000
resultado = []
for numero in listado:
    numero_doblado = numero * 2                 # Lo doblo
    numero_dividido = numero_doblado / 3        # Lo divido entre 3
    numero_redondeado = round(numero_dividido)  # Lo redondeo
    numero_sumado = numero_redondeado + 5       # Le sumo 5
    if numero_sumado % 2 == 0:                  # Si es par
        resultado.append(numero_sumado)         # Lo añado al resultado
print("El resultado final (Programación imperativa) es:", resultado)

# Este proceso si lo ejecuto con muchos datos
# Mi máquina tiene 18 cores.. con 2 hilos por core -> 36 hilos
# Y ese programa está usando un solo core virtual de mi máquina.. que pone al 100%
# El resto de cores virtuales están al 0% = 1/36 = 2.77% de uso de CPU
# Quién ejecuta el código de mi programa? Quién transporta las instrucciones a la CPU es un hilo de ejecución (THREAD)
# Esos hilos son gobernados por el sistema operativo
# Al arrancar un proceso, el SO crea un hilo principal (main thread) que es el que ejecuta el código de mi programa
# En un momento dado puedo abrir más hilos de ejecución (threads) para que hagan tareas en paralelo

# Qué ventajas me da, el haberlo hecho con el modelo map/reduce (en nuestro caso, usando Spark)?