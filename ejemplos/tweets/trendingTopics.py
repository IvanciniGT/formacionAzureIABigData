from pyspark import SparkContext, SparkConf
import re

conf = SparkConf().setAppName("Mi primera aplicación Spark").setMaster("local[2]")
sc = SparkContext(conf=conf)

listado = [
    "Preparando el examen de física de recuperación #MierdaDeVerano #StudyHard",
    "Nada como un buen libro en la playa #Relax #GoodVibes",
    "En la playa con amigos #SummerLove#GoodVibes",
    "Disfrutando del sol #SummerLove #BeachTime"
]

palabras_prohibidas = ["caca", "culo", "pedo", "pis", "mierda"]
N = 3
rdd = sc.parallelize(listado) # Esta función devuelve un tipo de dato llamado RDD (Resilient Distributed Dataset)

# Paso 1. Separamos los potenciales hashtags del texto
# Paso 2. Separamos las palabras .. y especialmente los hashtags
# Para eso usamos una expresión regular
# Paso 3. Unimos todas esas listas en una sola lista plana
# En realidad, paso 2 y 3 los hacemos a la vez con flatMap= map + flatten
# Paso 4: Nos quedamos solo con las palabras que empiezan por # = los hashtags
# Definimos una función de tipo predicate (devuelve True o False) que nos dice si una palabra es un hashtag
# Paso 5: Convertir los hashtags a minúsculas para evitar duplicados por mayúsculas/minúsculas
# Paso 6: Quitar ya el simbolo #
# Paso 7: Filtramos los hashtags que contienen palabras prohibidas
# def no_contiene_palabras_prohibida(hashtag):
#    for palabra_prohibida in palabras_prohibidas:
#        if palabra_prohibida in hashtag:
#            return False
#    return True
# Esa función de arriba es equivalente a esta otra:
# lambda hashtag: len([palabra_prohibida for palabra_prohibida in palabras_prohibidas if palabra_prohibida in hashtag] ) == 0 

# Paso 8: Llega el momento de contar... y no va a ser sencillo
# Al trabajar con map/reduce, tenemos que acomodarnos a las funciones que nos ofrecen
# Y para contar, la función que tenemos es reduceByKey
# reduceByKey trabaja sobre pares clave/valor
# Así que tenemos que transformar nuestro RDD de hashtags en un RDD de pares (hashtag, 1)
# De esa forma, al aplicar reduceByKey con la función suma, vamos a conseguir el conteo de cada hashtag
# Es muy artificial... pero es lo que hay con map/reduce

# Paso 9: Ordenar los resultados por número de apariciones (el valor del par clave/valor)
# Paso 10: Quedarnos con los N primeros
regex_particionado = r"[ .,;:_()[\]{}\"'¿?¡!-]+" # regex101.com
resultado = rdd.map( lambda tweet: tweet.replace("#", " #") ) \
    .flatMap(     lambda tweet: re.split(regex_particionado, tweet) ) \
    .filter(      lambda palabra: palabra[0] == "#" ) \
    .map(         lambda hashtag: hashtag.lower() ) \
    .map(         lambda hashtag: hashtag[1:] ) \
    .filter(      lambda hashtag: len([palabra_prohibida for palabra_prohibida in palabras_prohibidas if palabra_prohibida in hashtag] ) == 0 ) \
    .map(         lambda hashtag: (hashtag, 1) ) \
    .reduceByKey( lambda a, b: a + b ) \
    .sortBy(      lambda pareja: pareja[1], ascending=False ) \
    .take(N) # Aqui es donde mando toda la colección de postits al cluster... para que allí se procese!
# Esto es tan complejo que la gente de Spark creó una librería adicional llamada SparkSQL
# Que permite hacer muchas de estas operaciones usando sintaxis parecida a SQL
# Si bien, con esa sintaxis no podemos hacer todo lo que podemos hacer con map/reduce
# Agrupar por clave, contar, ordenar, filtar.. sin problema
# Aplicar transformaciones complejas de los datos ya es más difícil (como nuestros split, replace, etc)

print("El resultado final es:", resultado)

sc.stop()

# Las funciones map se ejecutan en modo lazy(perezoso) 
#       Realmente no se se ejecutan hasta que su resultado no es necesario
#       Cuando hemos hecho .map( lambda palabra: palabra.replace("#", " #") ) No estamos reemplazando nada aún
#       Solo estamos pidiendo que se ANOTE que hay que hacer eso.
#       Es como si tengo una carpeta con papeles (colección de datos) 
#       Y cada funcion map lo que hace es simplemente pegar un post-it en la carpeta diciendo "Cuando uses estos papeles, antes haz esto"
# Por contra, las funciones reduce se ejecutan en modo eager (ansioso)
#       Cuando hacemos un takme(N) es cuando hacen falta los datos
#       Ahí es cuando Spark mira todos los post-it que hay pegados en la carpeta
#       Y entonces empieza a ejecutar todas las operaciones map anotadas en los post-it