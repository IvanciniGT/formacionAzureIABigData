# IAs

Por IA hoy en día nos referimos principalmente a modelos de Deep Learning: Redes Neuronales con muchas capas (Deep Neural Networks).

    Red Neuronal: Es una función matemática -> Función de un programa de computadora (python)
                  que dadas un montón de variables de entrada (features) 
                  devuelven una salida: un único valor o un conjunto de valores.

    La función no la creamos nosotros, sino que le pedimos a una computadora que la genere.
    Y la genera de forma que para un conjunto de datos de entrada, se produzcan salidas que sean 
    lo más similares posible a datos historiales que ya conocemos.

        def modelo_ia(entrada1, entrada2, ..., entradan):
            # muchos cálculos matemáticos
            return salida

        def perceptron1(entrada1, entrada2, ..., entradan):
            # cálculos matemáticos
            return salida  # Número

        def perceptron1_capa2(salidaPerceptro1, salidaPerceptro1_2, salidaPerceptro1_3, ..., salidaPerceptro1_m):
            # cálculos matemáticos
            return salida  # Número

        E1 --- P1 --- P1(2)
           \ /    \ /
            x      x
           / \    / \
        E2 --- P2 --- P2(2)
           \ /
            x
           / \
        E3 --- P3 --- P3(2)
           \ /
            x
           / \    --- Pk(2)
        ...    ...
        En --- Pm

        así ponemos muchas capas

        Cada perceptrón es una función matemática simple que toma varias entradas y produce una salida.

        Las funciones matemáticas que usamos en los perceptrones son funciones matemáticas conocidas, como:
        - Función sigmoide
        - Función ReLU (Rectified Linear Unit)
        - Función softmax
        - tanh

    def perceptronN_capaM(entrada1, entrada2, ..., entradan):
        # cálculos matemáticos
        x = Coeficiente1 * entrada1 + Coeficiente2 * entrada2 + ... + Coeficienten * entradan + Bias
        # función de activación
        return e(x) - e(-x) / e(x) + e(-x)  # tanh

    tanh = e(x) - e(-x) / e(x) + e(-x)

        Cuando definimos una red, decimos:
        - cuantas capas tiene
        - cuántos perceptrones hay en cada capa
        - qué función de activación usamos en los perceptrones de cada capa

    Hay que calcular todos esos coeficientes y bias para cada perceptrón de la red.

    Si tengo una red de 4 capas, con 
    Primera capa 100 perceptrones
    Segunda capa 50 perceptrones
    Tercera capa 20 perceptrones
    Cuarta capa 5 perceptrones

    Recibe 100 entradas

    Cuántos parámetros tiene esa red?
        Las 100 entradas se conectan a los 100 perceptrones de la primera capa:
            Cada perceptrón tiene 100 coeficientes + 1 bias = 101 parámetros
            100 perceptrones * 101 parámetros = 10.100 parámetros
        Las salidas de esos 100 perceptrones se conectan a los 50 perceptrones de la segunda capa:
            Cada perceptrón tiene 100 coeficientes + 1 bias = 101 parámetros
            50 perceptrones * 101 parámetros = 5.050 parámetros
        Las salidas de esos 50 perceptrones se conectan a los 20 perceptrones de la tercera capa:
            Cada perceptrón tiene 50 coeficientes + 1 bias = 51 parámetros
            20 perceptrones * 51 parámetros = 1.020 parámetros
        Las salidas de esos 20 perceptrones se conectan a los 5 perceptrones de la cuarta capa:
            Cada perceptrón tiene 20 coeficientes + 1 bias = 21 parámetros
            5 perceptrones * 21 parámetros = 105 parámetros

    Total parámetros = 10.100 + 5.050 + 1.020 + 105 = 16.275 parámetros

    Que no tengo ni puñetera idea de que son, ni de cuanto valen.
    
    Lo que hago es pedirle a la computadora que juegue con esos parámetros (que se invente al azar unos valores iniciales para esos parámetros y los vaya modificando poco a poco) hasta que la ecuación de la red produzca salidas que se parezcan lo máximo posible a los datos históricos que le he dado.

Normalmente no calculamos redes nosotros. No tenemos pasta... Ni en la empresa lo hacemos. No tenemos pasta!
Hay gente que se dedica a entrenarlas. Y son 10 grandes:
- OpenAI (GPTs + O )
- Google (Bard + Gemini + BERT + PaLM)
- Microsoft (Sydney + Turing)
- Meta (LLaMA + BlenderBot)
- Anthropic (Claude)
- ...

Esos modelos en la mayor parte de los casos se ponen a disposición de la gente de forma gratuita.
En otros casos no... son de pago por uso.

Hay empresas que se dedican en cuerpo y alma a la creación de modelos (Anthropic, OpenAI, Cohere, AI21 Labs, ...). Esa gente los vende.
Luego hay empresas que no se dedican (su core) no es crear modelos, pero crean modelos para sus propios productos (Google, Microsoft, Meta, Amazon, ...). Esa gente los deja gratis en la mayor parte de los casos. Lo que tratan de evitar es denuncias por monopolio y posición dominante en el mercado.

Hoy en día quien tiene una buena IA tiene una posición de poder en el mercado enorme. 
Y solo empresas muy grandes pueden permitirse crear sus propios modelos.
Eso limita la entrada de nuevos competidores en el mercado.
Para evitarse denuncias por monopolio, esas grandes empresas ponen sus modelos a disposición de todo el mundo de forma gratuita (o casi gratuita).

Realmente esas redes neuronales se entregan a trozos... Lo que se entrega es una parte de la red neuronal... la que ha llegadoa aprender conceptos.

  > Soy una compañía de seguros de vehiculos.
    Quiero una IA (red neuronal) que me ayude a calcular el riesgo de un cliente -> Me a dar un parte o no.
    Tengo datos históricos de clientes y partes.

        Edad
        Sexo
        Kms anuales
        Años de carnet
        Tipo de vehículo
        Zona de residencia
        Denuncias previas por beber
        Número de partes de años anteriores
        ...

        Probabilidad de que una persona dé un parte. Que FACTORES tienen relación con que una persona dé un parte?
        - Su experiencia al volante                        A más edad   -> más experiencia
                                                           A más Kms anuales -> más experiencia
        - Su nivel de exposición al riesgo
                                                           A más Kms anuales -> más exposición 
        - Sus reflejos/su capacidad física al volante      A menos edad -> mejores reflejos
        - Su nivel de agresividad conduciendo              A menos edad -> más agresividad
        - Las características del vehículo
        - Su nivel de responsabilidad                      A más edad   -> más responsabilidad


        Esos datos, tienen relación con la probabilidad de que un cliente de un seguro me vaya a dar un parte?
            No.. no tienen relación DIRECTA!
            De hecho es mucho más complejo.

Quiero hacer un programa que sea capaz de dada una foto de un dígito manuscrito,
decirme qué dígito es (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

Voy a generar una función que devuelva true o false: 0 | 1
  hay_mas_puntos_a_la_izquierda_que_a_la_derecha
  hay_mas_puntos_arriba_que_abajo
  hay_el_mismo_numero_de_puntos_en_la_parte_superior_que_en_la_inferior
  hay_el_mismo_numero_de_puntos_en_la_parte_izquierda_que_en_la_derecha
  hay_mas_puntos_en_la_diagonal_topleft_a_bottomright_que_en_la_diagonal_topright_a_bottomleft
  hay_el_mismo_numero_de_puntos_en_la_diagonal_topleft_a_bottomright_que_en_la_diagonal_topright_a_bottomleft
  hay_mas_puntos_en_el_centro_que_en_los_alrededores

Si esas funciones me dicen:
- Que hay el mismo número de puntos (aproximadamente-10%) en la parte izquierda que en la derecha
- Que hay el mismo número de puntos (aproximadamente-10%) en la parte superior que en la inferior
  Eso significa que mi imagen es simétrica en ambos ejes -> podría ser un 0, un 8, un 1
    Podría ser un 3?

  ^^^^
  Con mas casos es la función principal, que luego llama a su vez a las funciones secundarias.


    Imagen de 100 pixels x 100 pixels = ICONO de 10.000 pixels

    Pix1        -- hay_mas_arriba_que_abajo            ---    función_detecta_0
    Pix2        -- hay_mas_izquierda_que_derecha.      ---    función_detecta_1
    ...         -- hay_igual_numero_arriba_que_abajo.  ---    función_detecta_2
    Pix10000    --  20 funciones que devuelven 0 | 1   ---    función_detecta_9
    
                    ^^^^^^^^^^
                    Aprendizaje

                    Nota: Este mismo aprendizaje podría usarlo no solo para decir si lo que hay dentro es un dígito del 0 al 9. Por ejemplo podría usarlo para decirme si lo que hay dentro es un número par o impar.
                    O si la figura es simétrica o no.

    La función de detección que dé el valor más alto es la que tomo como referencia para determinar el dígito.

    Cuandop montamos una red neuronal, lo que hacemos es básicamente esto!
    En este caso tengo una red que en primera capa tiene 20 perceptrones (cada uno de ellos es una función que devuelve 0 | 1) (sigmoide, ReLU, tanh, ...)
    Luego en la segunda capa tengo otros 10 perceptrón que toma las salidas de esos 20 perceptrones y calcula 10 salidas (una por cada dígito del 0 al 9)

    Y ya luego lo que tomo es el mayor valor de esos 10 perceptrones -> otra función matemática = otro perceptrón en tercera capa.

    Ahora lo que pido a la computadora es que me calcule los parámetros de esa red neuronal (los coeficientes y bias de cada perceptrón) para que dadas las imágenes de dígitos manuscritos que le doy (datos históricos) me devuelva el dígito correcto.

    
  que se llame: hay_mas_puntos_a_la_izquierda_que_a_la_derecha(todos los puntos de la imagen = array)
    ancho = array[0].length
    alto = array.length
    contador_izquierda = 0
    contador_derecha = 0
    for y in range(alto):
        for x in range(ancho):
            if array[y][x] == 1:
                if x < ancho / 2:
                    contador_izquierda += 1
                else:
                    contador_derecha += 1   
    return contador_izquierda > contador_derecha

En el mundo actual, las redes neuronales tienen millardos de parámetros (billones de los americanos):
    ???.000.000.000
Entrenar esas redes es extraordinariamente caro en tiempo de computación y dinero.
Solo las grandes empresas pueden permitírselo.
Esas empresas me dan no una red neuronal entera, sino la parte inicial que ya ha aprendido conceptos generales:
    - Hay más puntos a la izquierda que a la derecha
    - Hay más puntos arriba que abajo
    - Hay simetría horizontal
    - Hay simetría vertical
Lo que hago yo es tomar una de esas redes ya entrenadas y la adapto a mi problema concreto, es decir:
LE AÑADO UNA O VARIAS CAPAS FINALES QUE SIRVAN PARA MI PROBLEMA CONCRETO.
Y esa parte final es la que yo entreno con mis datos históricos => RAPIDO y BARATO.

Todo lo que son redes gratuitas las encuentro en una página web + librería de python llamada HuggingFace.
A parte, muchos clouds me ofrecen acceso a esos trozos de redes y además a las otras empresas de pago.
    Y me ofrecen infraestructura para entrenar entrenar nuevas capas que yo quiera añadir a esos trozos de redes.
    Y me generan en automático el programa python que necesito para entrenar esas nuevas capas.
    Y me facilitan la carga de mis datos históricos.
    Y una vez entrenada la red, me facilitan la puesta en producción de esa red para que mis aplicaciones la puedan usar.
    Me proporcionan un programa que puedo llamar por HTTP pasando datos de entrada y me devuelve datos de salida.
    Y ese programa lo que hace es recibir mis datos de entrada, pasarlos por la red neuronal y devolverme los resultados (JSON). 
    Y me dan infraestructura donde se instala esa red neuronal y el servicio web que la usa.
    TODO ESO ME LO REGALAN (€€€)

 En los clouds va a más... Como más o menos todos tenemos las mismas necesidades, me entrenan (añaden la mejor arquitectura de capas detras del trozo de red neuronal que yo les digo que quiero usar) y pa'lante!

 Esto es lo que me ofrece el IA Forge de Azure -> rebautizado como      Azure AI Service.
                                                                        Azure OpenAI Service

IA Studio:
    - Voice Studio
    - Vision Studio
    - Language Studio
    - 

 400 Billones americanos de parámetros son en españa: 400 Millardos de parámetros. = 400.000.000.000
 Cada uno de esos es un double (8 bytes) = 3,2 TB de RAM solo para cargar la red en memoria.

 31.000.000 de horas! 
 31.000.000 horas / 8760 horas/año = 3.534 años de computación en una sola GPU
 Lo que pasa es que no usamos una sola GPU.. Usamos muchas GPUS... Si uso 10.000 GPUs en paralelo:
    3.534 años / 10.000 = 0,3534 años = 4,24 meses

---

# Programación funcional

En el mundo de la programación teenemos lo que denominadas paradigmas de programación.
Eso realmente es solo un nombre "hortera" que le damos a las distintas formas en las que podemos usar un lenguaje para expresarnos. No es algo exclusivo de los lenguajes de programación. En español, inglés, catalán, vasco, ... también tenemos distintas formas de expresarnos (no les llamamos paradigmas a esas formas, pero podrían serlo).

> Felipe, pon una silla debajo de la ventana.               IMPERATIVO
> Felipe, debado de la ventana tiene que haber una silla.   DECLARATIVO

En el mundo del desarrollo, algunos de los paradigmas más utilizados son:
- Imperativo                Es la mayor parte del código que escribimos.
                            Le decimos a la computadora lo que debe ir haciendo... paso a paso. La computadora debe ejecutarlo secuencialmente.
                            A veces necesitamos romper la secuencialidad, y salen las típicas estructuras de control (if, for, while, switch, ...)
- Procedural                Es una evolución del imperativo.
                            Cuando el lenguaje me permite agrupar muchas de esas instrucciones en un bloque al que le pongo un nombre y posteriormente invocar / solicitar la ejecución de ese bloque por su nombre decimos que el lenguaje soporta programación procedural.
                            Esos bloques, dependiendo del lenguaje, pueden llamarse funciones, procedimientos, métodos, subrutinas, ...
                            Beneficios:
                            - Reutilización de código
                            - Mejor organización del código
- Orientado a objetos       Los programas que creamos manejan datos. Y esos datos son de un determinado tipo.
                            Todo lenguaje viene con una serie de tipos de datos por defecto. Cada uno se caracteriza por unas propiedades y comportamientos concretos.
                            En la programación orientada a objetos, podemos crear nuestros propios tipos de datos (clases) definiendo sus propiedades (atributos) y comportamientos (métodos).
                                        
                                        Se caracteriza por                 Comportamientos:
                            Texto       Una secuencia de caracteres        ponerEnMayúsculas(), ponerEnMinúsculas(), ...
                            Fecha       día, mes, año                      sumarDías(), siCaeEnFinDeSemana(), ...

                            Todo lenguaje maneja tipos de datos y vienen con unos cuantos de ellos por defecto.
                            JS y Python tienen tipos de datos?

                            JS:             Python
                                Number      int, float
                                String      str
                                Boolean     bool

                            JS o python son lenguajes de tipado dinámico o débil.
                            Qué significa eso, que las variable NO TIENEN TIPO.

                            ```java
                               String nombre = "Felipe"; // Asignando la variable nombre al valor "Felipe"
                            ```
                            ```js
                               var nombre = "Felipe"; // Asignando la variable nombre al valor "Felipe"
                            ```
                            ```python
                               nombre = "Felipe"; # Asignando la variable nombre al valor "Felipe"
                            ```
                            El concepto de variable cambia de lenguaje a lenguaje.
                            Una variable no es una cajita donde pongo cosas y luego las saco. Al menos no en JAVA, PYTHON o en JS (y son los lenguajes que más usamos).
                            En C o C++ si que es así.
                            En JAVA, PYTHON o JS una variable tiene más que ver con el concepto de puntero en C.

                            Esa línea de código en JAVA, JS o PYTHON lo que hace es:
                             1. "Felipe"   -> JAVA:   Crea un dato de tipo String en memoria RAM con el valor "Felipe"
                                              JS:     Crea un dato de tipo string en memoria RAM con el valor "Felipe" 
                                              Python: Crea un dato de tipo str en memoria RAM con el valor "Felipe"
                             2. String nombre --> Java: Crea una variable llamada nombre que puede apuntar a objetos de tipo String... o derivados.
                                                  JS:     Crea una variable llamada nombre
                                                  Python: Crea una variable llamada nombre
                             3. =           --> Asigna a la variable nombre al dato creado en RAM.
                            
                            ```java | js | python
                                nombre = "Antonio";
                            ```
                            Esa línea de código lo que hace es:
                                1. "Antonio"   -> JAVA:   Crea un dato de tipo String en memoria RAM con el valor "Antonio"
                                                  JS:     Crea un dato de tipo string en memoria RAM con el valor "Antonio" 
                                                  Python: Crea un dato de tipo str en memoria RAM con el valor "Antonio"
                                                  La pregunta es dónde se crea ese dato en memoria RAM? En el mismo sitio que "Felipe" o en otro sitio distinto? En otro sitio distinto.
                                                  Y en este momento tengo en memoria 2 datos distintos:
                                                    Dato1: "Felipe"
                                                    Dato2: "Antonio"
                                2. nombre =   --> mover la variable que esta pegada al lado del dato "Felipe" 
                                                    y ponerla pegada al lado del dato "Antonio"

                                                  Y al hacer esto, el dato "Felipe" ya no tiene ninguna variable que apunte a él.
                                                  Y por ende se convierte en BASURA (Garbage).
                                                  Y potencialmente (espero.. aunque no se si pasará) ese dato "Felipe" será eliminado de memoria RAM en algún momento por el Garbage Collector (que es un proceso que existe en JVM, en V8 de JS y en el intérprete de Python que se encarga de eliminar datos que ya no tienen ninguna variable apuntando a ellos para liberar memoria RAM).

                                                  En C el comportamiento habría sido distinto. El dato "Felipe" habría sigo sobreescrito con "Antonio".
                                Hay lenguajes en los que las variables tienen tipo: Son los lenguajes de tipado estático o fuerte.
                                Hay lenguajes en los que las variables no tienen tipo: Son los lenguajes de tipado dinámico o débil.
                                   En estos, una variable puede apuntar a datos de cualquier tipo.
                                
                                Lo que hay además es lenguajes que me permiten definir mi propio tipo de datos (clases), con sus propias propiedades (atributos) y comportamientos (funciones). Cuando un lenguaje me permite hacer eso, decimos que es un lenguaje que soporta el paradigma de programación orientada a objetos.

                                                                    Sus características son:            Comportamientos:
                                Tipo de datos custom: Usuario.      nombre, email,                      cambiarContraseña(),       
                                                                    contraseña, fechaRegistro           enviarEmailVerificación(), ...
                                                                    

                                Luego hay más características aquí, algunas soportadas por unos lenguajes, otras por otros:
                                 herencia (simple o múltiple), polimorfismo, encapsulación, sobrecarga de métodos, sobreescritura de métodos, interfaces, ...

Hay un paradigma, viejo... con muchos años.. más que el paradigma de orientación a objetos, que últimamente ha tomado mucha fuerza.
Es el paradigma de programación funcional.

- Paradigma funcional           Cuando el lenguaje me permite que una variable apunte a una función y posteriormente
                                invocar / solicitar la ejecución de esa función a través de esa variable, decimos que el lenguaje soporta programación funcional.
                                Java, JS, Python, C#, Ruby, ... Todos ellos soportan programación funcional.

                                En tema no es lo que es la programación funcional.. que es una chorrada a nivel conceptual.
                                El tema es lo que puedo hacer cuando el lenguaje soporta programación funcional:
                                - Puedo crear funciones que acepten funciones como parámetros de entrada.
                                - Puedo crear funciones que devuelvan funciones como resultado de salida: Closures.
                               
                               Al usar paradigma funcional, creamos funciones por 3 motivos:
                               - Para reutilizar código
                               - Para organizar mejor el código
                               - Para poder pasar funciones a otras funciones que quiero usar y que me exigen por articulo 33 que les pase funciones como parámetros de entrada.
# Modelo de programación MapReduce

Es un modelo, ideado originalmente por Google, para procesar grandes volúmenes de datos. La gracia es que soporta procesamiento distribuido y paralelo. Es decir, cuanto planteo el algoritmo de esta forma (en lugar de otras formas) puedo paralelizar el procesamiento de los procesos quee quiera aplicar sobre los datos.

Cualquier procesamiento que quiera hacer sobre un conjunto de datos, lo puedo plantear como una serie de pasos Map y Reduce.

Un algoritmo map reduce es UNA SOLA LINEA DE CODIGO.

Este modelo de programación se basa en 2 tipos de funciones:
- Funciones de tipo MAP
- Funciones de tipo REDUCE
De ahí su nombre: MapReduce

El esquema es siempre el mismo:

    DATOS DE ENTRADA     --> Aplico una función de tipo MAP   -->  DATOS INTERMEDIOS 1
    DATOS INTERMEDIOS 1  --> Aplico otra función de tipo MAP  -->  DATOS INTERMEDIOS 2
    ...
    DATOS INTERMEDIOS N  --> Aplico una función de tipo REDUCE -->  RESULTADO FINAL

Al menos necesito 1 función de tipo MAP y 1 función de tipo REDUCE.
Funciones de tipo Map puedo tener tantas como quiera.
Funciones de tipo Reduce solo 1 y al final.

Qué es una función de tipo MAP?
  Es una función que al aplicarla sobre un conjunto de datos que acepte programación map reduce, me devuelve otro conjunto de datos que siga aceptando programación map reduce.

  Hay un montón de funciones de tipo MAP conocidas:
    - Función "map"
    - Función "filter"
    - Función "sort"
    - Función "groupBy"
    - Función "flatMap"
    - ...

Qué es una función de tipo REDUCE?
  Es una función que al aplicarla sobre un conjunto de datos que acepte programación map reduce, me devuelve lo que sea que ya no acepte programación map reduce.

  Hay un montón de funciones de tipo REDUCE conocidas:
    - Función "reduce"
    - Función "count"
    - Función "sum"
    - Función "average"
    - Función "min"
    - Función "max"
    - Function "collect"
    - ...
  
 
 COLECCION INICIAL 
 DE DATOS
    1
    2
    3
    4

Voy a multiplicar cada uno de esos datos x2       Aquí hemos usado una función de tipo MAP: la función "map"
                                                        Con una función de mapeo: doblar
    2
    4
    6
    8

Quiero quedarme solo con los datos mayores que 4    Aquí hemos usado otra función de tipo MAP: la función "filter"
                                                        Con una función de filtrado: esMayorQue4

    6
    8

Quiero sumarlos                                    Aquí hemos usado una función de tipo REDUCE: la función "sum"

    14

Dependiendo del lenguaje, este código se verá de una forma u otra.. pero muy similar a:

   coleccionInicial
         .map(doblar)
         .filter(esMayorQue4)
         .sum()

- La función "map" es una función que: 
      Aplica una función de mapeo (transformación) sobre cada uno de los elementos de la colección inicial
      Va añadiendo los resultados a una nueva colección que devuelve como resultado.

      Podríamos definirla más o menos así:

        ```python
        def map(coleccion, funcion_mapeo):
            nueva_coleccion = []
            for elemento in coleccion:
                nuevo_elemento = funcion_mapeo(elemento)
                nueva_coleccion.append(nuevo_elemento)
            return nueva_coleccion
        ```
      Es decir, me permite transformar cada uno de los elementos de una colección en otro elemento distinto, creando una nueva colección con esos nuevos elementos.
- La función "filter" es una función que:
      Aplica una función de filtrado (condición) sobre cada uno de los elementos de la colección que recibe como entrada
      Si el resultado de aplicar la función de filtrado es true, añade ese elemento a una nueva colección que devuelve como resultado.

      ```python

        def esMayorQue4(elemento): # Es una función de tipo predicado
            return elemento > 4 # Devuelve True o False. Un boolean

        def filter(coleccion, funcion_filtrado):
            nueva_coleccion = []
            for elemento in coleccion:
                if funcion_filtrado(elemento):
                    nueva_coleccion.append(elemento)
            return nueva_coleccion
        ```

        Dicho de otra forma, me permite quedarme solo con los elementos de una colección que devuelven true al aplicarles una función de filtrado (condición).
- La función "sum" es una función que:
      Suma todos los elementos de la colección que recibe como entrada y devuelve el resultado como un único valor.


Eso mismo, lo podría expresar en lenguaje imperativo:

```python
    datos = [1, 2, 3, 4]
    suma = 0
    for dato in datos:
        resultado = dato * 2
        if resultado > 4:
            suma += resultado
```

En programación funcional:

```    
    datos = [1, 2, 3, 4]
    datos.map(doblar)
         .filter(esMayorQue4)
         .sum();

```

---

Este caso es una chorrada.

Vamos a hacer un caso más interesante: Generar los trending topics de twitter (ahora X)... mediante programación mapReduce.

Colección inicial de tweets (los tweets que me llegan en el último minuto):

    Tweet1: "En la playa con amigos #SummerLove#GoodVibes"
    Tweet2: "Disfrutando del sol #SummerLove #BeachTime"
    Tweet3: "Preparando el examen de física de recuperación #MierdaDeVerano #StudyHard"
    Tweet4: "Nada como un buen libro en la playa #Relax #GoodVibes"

Quiero conseguir:

    SummerLove: 2
    GoodVibes: 2
    BeachTime: 1
    StudyHard: 1
    Relax: 1

De donde he eliminado el hashtag #MierdaDeVerano? Porque contiene palabras prohibidas: Caca Culo Pedo Pis Mierda

---

    Tweet1: "En la playa con amigos #SummerLove#GoodVibes"
    Tweet2: "Disfrutando del sol #SummerLove #BeachTime"
    Tweet3: "Preparando el examen de física de recuperación #MierdaDeVerano #StudyHard"
    Tweet4: "Nada como un buen libro en la playa #Relax #GoodVibes"

    vvvv

    Hacer un replace en cada texto del "#" por " #"

    Hemos aplicado la función "map", pasando como función de mapeo una función que hace un replace del "#" por " #".

---

    Tweet1: "En la playa con amigos #SummerLove #GoodVibes"
    Tweet2: "Disfrutando del sol #SummerLove #BeachTime"
    Tweet3: "Preparando el examen de física de recuperación #MierdaDeVerano  #StudyHard"
    Tweet4: "Nada como un buen libro en la playa #Relax #goodvibes"

    vvvv

    Podría hacer un split de cada texto (por espacios, puntos, comas, (), [], -, ...)

    Hemos aplicado la función "map", pasando como función de mapeo una función que hace un split del texto en palabras.

---

    Lista de palabras 1 : "En,la,playa,con,amigos,#SummerLove,#GoodVibes"
    Lista de palabras 2 : "Disfrutando,del,sol,#SummerLove,#BeachTime"
    Lista de palabras 3 : "Preparando,el,examen,de,física,de,recuperación,#MierdaDeVerano,#StudyHard"
    Lista de palabras 4 : "Nada,como,un,buen,libro,en,la,playa,#Relax,#goodvibes"

    vvvv

    Unificar todas esas listas en una sola lista

    Hemos aplicado la función "flatten", que unifica todas las listas en una sola lista.

---

    En
    la
    playa
    con
    amigos
    #SummerLove
    #GoodVibes
    Disfrutando
    del
    sol
    #SummerLove
    #BeachTime
    Preparando
    el
    examen
    de
    física
    de
    recuperación
    #MierdaDeVerano
    #StudyHard
    Nada
    como
    un
    buen
    libro
    en
    la
    playa
    #Relax
    #goodvibes

    vvvv

    Filtrar solo las palabras que empiecen por "#"

    Hemos aplicado la función "filter", pasando como función de filtrado una función que devuelve true si la palabra empieza por "#".

---

    #SummerLove
    #GoodVibes
    #SummerLove
    #BeachTime
    #MierdaDeVerano
    #StudyHard
    #Relax
    #goodvibes

    vvvv

    Filtrar los hashtags que contengan alguna palabras prohibidas

    Hemos aplicado la función "filter", pasando como función de filtrado una función que devuelve true si la palabra NO contiene ninguna palabra prohibida.

---

    #SummerLove
    #GoodVibes
    #SummerLove
    #BeachTime
    #StudyHard
    #Relax
    #goodvibes

    vvvv

    Quitar el "#" de cada hashtag

    Hemos aplicado la función "map", pasando como función de mapeo una función que quita el "#" del principio de cada hashtag.

---

    SummerLove
    GoodVibes
    SummerLove
    BeachTime
    StudyHard
    Relax
    goodvibes

    vvvv

    pongo los hashtags en minúsculas

    Hemos aplicado la función "map", pasando como función de mapeo una función que convierte cada hashtag a minúsculas.

---

    summerlove
    goodvibes
    summerlove
    beachtime
    studyhard
    relax
    goodvibes

    vvvv

    Agrupar por hashtag y contar ocurrencias

    Hemos aplicado la función "groupBy", pasando como función de agrupación una función que agrupa por hashtag.
    Y como función de reducción una función que cuenta ocurrencias.

---

    summerlove: 2
    goodvibes: 2
    beachtime: 1
    studyhard: 1
    relax: 1