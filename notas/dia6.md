

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

    PERRO:  ANIMAL, MASCOTA, LADRAR, HUESO, JUGAR, PASEAR, AMIGO
    CASA:  HOGAR, FAMILIA, TECHO, PUERTA, VENTANA, COCINA, DORMIR
    Lo que se hizo fue representar esas palabras en un espacio N-DIMENSIONAL

        Eje X:  Ser vivo
        Eje Y:  Tamaño
        Eje Z:  Temperatura
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

En google, al hombrecillo este se le ocurrio un nuevo modelo de red neuronal:  "Transformers"
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

Esta arquitectura se usó por primera vez para traducir textos (Google Translate):  BERT.

ROBERT, GPT, T5, PaLM, LLaMA... son variantes de Transformers adaptadas a diferentes usos.

---

Tenemos que cargar un huevo de preguntas y sus respuestas.
Con las respuestas le damo lo que é debe contestar a preguntas del "tipo" que le pasamos.
Podemos llegar a pensar que esto es al final una BBDD de pares pregunta-respuesta.
Pero no es así.
Aquí se usa luego un modelo de lenguaje grande (LLM) para que entienda la pregunta y busque en su memoria la respuesta más adecuada.

---

# Questions and Answers (Q&A)

Tendremos varias cosas: 
- Bot conversacional (app)
- Servicio REST (modelo de lenguaje grande - LLM)
  - A ese servicio le pasamos la pregunta
  - El servicio intenta entender la pregunta (usando el modelo de lenguaje grande)
  - El servicio busca en el índice de preguntas/respuestas la respuesta más adecuada
  - El servicio devuelve (JSON) la respuesta al bot conversacional
- Índice de preguntas/respuestas
  - Motor de búsqueda (Azure Search)
  - Índice construido a partir de las preguntas y respuestas que hemos cargado

El índice se genera desde la base de conocimientos (Knowledge Base)
  - Conjunto de documentos (PDFs, Word, HTML, TXT...)
  - Se extraen preguntas y respuestas de esos documentos (usando técnicas de NLP)
  - Se crean pares pregunta-respuesta
  - Se indexan en el motor de búsqueda
Lo que construimos es el knowledge base ... y ese knowledge base tiene que estar sometido a control de versiones.

    Yo aporto el knowledge base (documentos)
    Azure me : 
    - Genera un índice de preguntas/respuestas en Azure Search
    - Despliega un modelo de lenguaje grande (LLM) para entender las preguntas
    - Despliega un servicio REST que es capaz de recibir preguntas, entenderlas, buscar en el índice y devolver respuestas.
    - Opcionalmente puedo desplegar un bot conversacional (chatbot) que use ese servicio REST para responder a los usuarios.
      Ese, en caso que lo quiera es otra app, que azure monta en c#, y que puedo descargar... y modificar a mi gusto. Se parte de una plantilla.
    - Esta app luego luego la compilo y despliego.. dónde? On premise o en Azure.
    - Si quiero desplegarla en Azure eso me lo regalan!

Lo que vamos construyendo, nuestro proyecto es el knowledge base -> Sujeto a control de versiones.
Para eeso me interesan varias cosas: 
- Subir URLs y no ficheros (menos aún andar con ediciones con las pantallitas)
- Jugar algo con las pantallitas... pero luego exportar todo a ficheros (json, yaml, md...)
- Poder versionar esos ficheros con git (github, azure repos...)

Y lo que desplegamos es el knowledge base.
Realmente lo que se hace es una copia del índice de preguntas/respuestas en Azure Search del entorno de pruebas al entorno de producción.

---

Al desplegarse, tendremos una URL totalmente funcional por la que podremos hacer peticiones REST para obtener respuestas a preguntas.

Y podré ir haciendo múltiples despliegues, a medida que vaya mejorando el knowledge base (añadiendo documentos, corrigiendo preguntas/respuestas...)

De alguna forma, Azure Forge <- Language Studio, me ayuda con un montón de cosas: 
- Creación y despliegue del knowledge base (índice de preguntas/respuestas) (MLOPs)
- Me dan la herramienta de indexado (Azure Search)
- Me dan el modelo de lenguaje grande (LLM) desplegado (en un entorno) y listo para usar
- Me dan el servicio REST que usa el LLM y el índice de preguntas/respuestas
- Ese servicio desplegado en un entorno de Azure (pruebas, producción...)

Me dan un montón de cosas... y además NO NECESITO NADA de conocimiento de IA, ML, ni desarrollo software (modelos, rest, apis de integración con indexadores...)

---

Sin olvidar que;
- Estamos desarrollando un software (mediante el knowledge base), pero un software
- Y por ende, debemos aplicar todas las buenas prácticas del desarrollo software
  - Control de versiones
  - Entornos de pruebas y producción
  - Pruebas unitarias, de integración, de sistema
  - Control de los despliegues
  - Monitorización
  - Seguridad
  - Gestión de costes
  - Gobernanza


---

POST 

https: //lenguajeivan.cognitiveservices.azure.com/language/: query-knowledgebases?projectName=PreguntasyRespuestasIvan&api-version=2021-10-01&deploymentName=production 
-H "Ocp-Apim-Subscription-Key:  "
-H "Content-Type:  application/json" 
-d "
{
    "top": 3",
    "question": "Qué carnet necesito",
    "includeUnstructuredSources": true,
    "confidenceScoreThreshold": "0.1",
    "answerSpanRequest": {
        "enable": true",
        "topAnswersWithSpan": 1",
        "confidenceScoreThreshold": "0.1"
    }",
    "filters": { }
}

--
curl -X POST "https://lenguajeivan.cognitiveservices.azure.com/language/:query-knowledgebases?projectName=PreguntasyRespuestasIvan&api-version=2021-10-01&deploymentName=production" -H "Ocp-Apim-Subscription-Key: " -H "Content-Type: application/json" -d "{\"top\":3,\"question\":\"Cualos tractores hay\",\"includeUnstructuredSources\":true,\"confidenceScoreThreshold\":\"0.1\",\"answerSpanRequest\":{\"enable\":true,\"topAnswersWithSpan\":1,\"confidenceScoreThreshold\":\"0.1\"}}"


---

La idea es que muchos procesos que tengo en la empresa los puedo autoamtizar MUY RAPIDO con estas tecnologías.
Antes necesitaba a una persona (o legión de personas) contestando preguntas de clientes.
Ahora puedo montar un bot conversacional en pocos días, que conteste a la mayoría de las preguntas de los clientes.

Puedo montar programas que mejoren la calidad de mis servicios sin esfuerzo prácticamente:
- Dame la foto del billete que ya saco yo todos los datos.

Si todo eso lo aplico a procesos ya existentes en la empresa, tengo datos a kilos para entrenar modelos de IA específicos para mi empresa.

Estoy con una app de gestión de expedientes de clientes.
Y hay un paso donde una persona necesita leer el expedientee y enrutarlo a un departamento u otro.
- En versión 1, montar un modelo que resuma el expediente y se lo pase a la persona. Le ahorro un huevo de tiempo.
- En versión 2, montar un modelo que lea el expediente y lo enrute automáticamente al departamento adecuado.

En las apps que montamos habitualmente, y en los procesos de negocio de las empresas, hay un montón de puntos donde podemos aplicar IA para mejorar la eficiencia y reducir costes.
---
De hecho en muchas ocasiones lo que montamos no es un modelo, son cadenas de modelos (pipeline)

IVR: Sistema de Respuesta de Voz Interactiva (IVR)

-> Llaman por telefono a una empresa. Capturo audio 
--> Lo mando a un modelo de speech to text (STT)
--> Proceso el texto con un modelo de lenguaje grande (LLM) para entender la intención del cliente
--> Según la intención, lo mando a un bot conversacional (chatbot) para que le conteste
--> La respuesta del bot la mando a un modelo de text to speech (TTS)
--> Devuelvo el audio al cliente

---

COSTES!

Es caro esto? NO... es ridículidamente barato! Si hecho bien las cuentas!
Son muchos las horas de trabajo que ahorro en personal, que es lo más caro de todo en la empresa.

Un banco tiene millones de peticiones al mes. Se le puede ir la factura a 10.000€ al mes en servicios de IA en Azure. La cuenta hay que echarla bien!

---

Son caros los clouds? Mucha gente opina que SI.

Resulta que por tener no se cuantos Tbs de almacenamiento en Azure, pago 7000€ al mes. Me vienen al año: 84.000€
LOCURA.. los de contabilidad COMO LOCOS!
A ti en HDD eso te cuesta 2000€ comprarlo.

No es solo HDD, es:
- Servidores donde montar los HDDs
- Instalación de SO y software de gestión de almacenamiento / parches, seguridad redes.
- Electricidad
- Refrigeración
- Personal de IT para gestionar todo eso (jefes de tios de redes, admins de sistemas, admins de almacenamiento...)

Si 85000€ son el salario de 2 personas.

Esto es una tendencia!

---

JAVA es un lenguaje que gestiona bien la ram o mal? COMO EL CULO!
Ahora la pregunta es Uso un lenguaje que gestione bien la RAM? o uso JAVA que la gestiona como el culo?

- Desarrollo en JAVA    200 h de desarrollador a 50€/h = 10.000€
- Desarrollo en C       300 h de desarrollador a 65€/h = 19.500€
Ostias... 9.500€ más caro el desarrollo en C.
Cuánto cuesta una pastilla de RAM pal servidor? 1000€.. JAVA sea.. Calidad peor... pero se hace y más barato.

---

AZURE contrato una BBDD -> 2000€ al mes. -> Año 24.000€
Me sale a cuenta tenerla on prem... Ya.. pero ahora mete el salario del administrador de BBDD. Solo con ese salario ya has pagado eso!