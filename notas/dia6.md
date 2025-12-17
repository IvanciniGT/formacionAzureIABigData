

2017 -> GOOGLE un ingeniero (un equipo) creo una arquitectura de red neuronal (paper)

Esa arquitectura lo cambió todo.
Hasta ese momento usabamos mucho un tipo de redes neuronales llamadas "redes neuronales convolucionales y recurrentes".

Ambas 2 arquitecturas tenían un objetivo (eran formas diferentes de conseguir un objetivo), conseguir que información que había procesado la red neuronal se mantuviera en el tiempo, para la toma de decisiones futuras.

> Escuchando audio. No puedo procesar un instante de tiempo, sin el contexto de lo que ha pasado antes.
Por ejemplo, para yo identificar una cancion, no me vale con ir escuchando segundo a segundo, sino que necesito escuchar un fragmento más largo, para identificar la canción.

Y los datos que ya he procesado los mantendo en memoria para poder tomar decisiones futuras (identificar la canción).

El escuchar un acorde por si solo no me da la canción. O el escuchar varios acordes pero sueltos en el tiempo o sin relación entre si, tampoco me da la canción.

> Traducir un texto o entender una frase.

No puedo traducir un texto yendo palabra por palabra, sino que necesito entender el contexto de la frase o del párrafo para poder hacer una buena traducción, o la frase no la voy a entender, ya que el significado de una palabra depende del contexto.

Los modelos de LLM tienen diccionarios de palabras que usamos igual que los dicccionarios de español.
Los ordenadores tienen sus diccionarios. 
- CASA
El significado de una palabra tiene que ver con qué palabras está relacionada esa palabra.

    PERRO: ANIMAL, MASCOTA, LADRAR, HUESO, JUGAR, PASEAR, AMIGO
    CASA: HOGAR, FAMILIA, TECHO, PUERTA, VENTANA, COCINA, DORMIR
    Lo que se hizo fue representar esas palabras en un espacio N-DIMENSIONAL

        Eje X: Ser vivo
        Eje Y: Tamaño
        Eje Z: Temperatura
        ...
        Monto 50.000 ejes (que no tengo npi de lo que son yo humano)

    Y medir la distnacia entre palabras.
    Si dos palabras son iguales en todos los ejes,salvo en 1 .. y en ese están muy lejos entre si, eso significa que son antonimos.
    Si dos palabras son muy cercanas en ese espacio N-DIMENSIONAL, significa que son sinónimos o están relacionadas.

    Una palabra se representa como un vector de puntuaciones en esos ejes.
    Hay muchos diccionarios... depende del número de ejes que usemos (número de dimensiones que analice). A má dimensiones, mejor representación /entendimiento tengo de las palabras.

    Herramientas como Word2Vec, GloVe, FastText... crean esos diccionarios de palabras en espacios N-DIMENSIONALES.

> Si lo llevo a una foto es el mismo concepto. El analizar un pixel (R,G,B) por si solo no me da información de la imagen, Ni el analizar cientos de pixels sueltos. Necesito analizar conjuntos de pixels relacionados entre si, para entender la imagen. Si un pixel está más cerca de otro o menos cerca eso me da información para entender qué es lo que estoy viendo en la imagen.


Esos modelo de red neuronal, lo que hacían era procesar un item... y su resultado se usaba como entrada adicional para procesar el siguiente item.

    Algo asi como si quiero traducir la frase:
    "El perro de mi vecino ladra por las noches"

        El          -> salida 0
        perro       -> salida 1
         + salida 0
        de          -> salida 2
         + salida 1
         + salida 0
  
Esta era la forma en la que lo hacíamos (red neuronal recurrente).

Más o menos algo salía bien, pero no del todo.

Para sonidos no iba mal. Pero en fotos y en textos no iba tan bien.

En google, al hombrecillo este se le ocurrio un nuevo modelo de red neuronal: "Transformers"
esto cambió el mundo de las redes neuronales y de las IAs.
Hoy en día prácticamente todas las IAs que vemos (LLMs, DALL-E, MidJourney, Stable Diffusion...) usan Transformers.

La explicación (que es dura) se da en un paper llamado "Attention is all you need".
Esos modelo procesar u texto, imagen, audio como un todo... no poco a poco (como se hacía con las redes recurrentes o convolucionales).

Tienen varias cabezas de lectura paralelas.. a más cabezas más capacidad de entendimiento y mejor es el modelo.. y mucho más cuesta entrenarlo y ejecutarlo.


    *  perro de mi vecino ladra por las noches
    El *     de mi vecino ladra por las noches
    El perro *  mi vecino ladra por las noches
    El perro de *  vecino ladra por las noches
    El perro de mi *      ladra por las noches
    El perro de mi vecino *     por las noches        
    El perro de mi vecino ladra *   las noches
    El perro de mi vecino ladra por *   noches
    El perro de mi vecino ladra por las *

Intenta buscar RELACIONES, qué palabras están relacionadas con qué palabras en el texto completo.

De alguna forma, es el comienzo de un análisis sintáctico y semántico del texto.

Ese análisis se repite en varias capas (layers) de la red neuronal, para ir refinando el entendimiento del texto. Cada capa nos da un nivel de agrupamiento superior.
Una capa al final es capaz de identificar sujeto/predicado
Otra capa es capaz de identificar sintagmas nominales, preposicionales, verbales...
Y eso mismo aplicado no solo intrafrase. Sino a nivel de párrafo, documento.

Estos modelos adminen un tamaño de texto máximo (4096 tokens, 8192 tokens, 32768 tokens... depende del modelo).

Modelos más potentes (GPT-4, PaLM2, LLaMA2...) son capaces de manejar textos más largos.

Esta arquitectura se usó por primera vez para traducir textos (Google Translate): BERT.

ROBERT, GPT, T5, PaLM, LLaMA... son variantes de Transformers adaptadas a diferentes usos.

---

Tenemos que cargar un huevo de preguntas y sus respuestas.
Con las respuestas le damo lo que é debe contestar a preguntas del "tipo" que le pasamos.
Podemos llegar a pensar que esto es al final una BBDD de pares pregunta-respuesta.
Pero no es así.
Aquí se usa luego un modelo de lenguaje grande (LLM) para que entienda la pregunta y busque en su memoria la respuesta más adecuada.