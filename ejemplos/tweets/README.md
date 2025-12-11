# Ejemplos con Spark

## Instación del entorno

```bash
python -m venv venv
# Para activarlo:
## En windows:
venv\Scripts\activate
### Nota: En windows, puede dar un error la activación del entorno virtual. 
### Si están deshabilitadas las políticas de ejecución de scripts, pueden habilitarlas con el siguiente comando en PowerShell (ejecutar como administrador):
# Set-ExecutionPolicy Unrestricted -Scope Process
## En macOS/Linux:
source venv/bin/activate

# Instalar spark.
# Es la gran librería del mundo bigdata (en paralelo con Hadoop).
pip install pyspark
```

## Acerca de Spark

Es un proyecto de la funcaión Apache que ofrece una implementación del modelo de programación MapReduce. Esta implementación es más eficiente que la de Hadoop, ya que permite el procesamiento en memoria y optimiza las operaciones de lectura y escritura en disco.

Es la base de muchos servicios cloud, como por ejemplo en Azure:
- Databricks
- Synapse 

Con esta librería podemos arrancar un cluster de máquinas, que van a trabajar en paralelo para procesar grandes volúmenes de datos.

También podemos crear programas que se ejecuten contra una de esas granjas/clusters de máquinas.

Cuando trabajamos desarrollando un programa Spark, una utilidad extra que nos ofrece la librería es la posibilidad de crear un cluster en nuestra máquina local con un solo nodo, para poder desarrollar y probar el código antes de desplegarlo en un cluster real.

Todo programa Spark tiene 5 partes principales:
1. Abro una conexión contra un cluster Spark (en local o remoto).
2. Mando al cluster los datos que quiero procesar.
3. Defino el algorimo map-reduce que quiero ejecutar contra esos datos.
4. Capturar los resultados y hacer lo que me interese con ellos.
5. Cerrar la conexión contra el cluster.

Cuando trabajamos desde un cloud, habitualmente los clouds me dan entornos de trabajo preconfigurados, donde ya tengo el cluster creado, donde:
- Los pasos 1 y 5 los gestiona el cloud.
- El paso 2 lo hago subiendo los datos a un almacenamiento del cloud (por ejemplo, un blob storage).
- El paso 4 lo hago guardando los resultados en un almacenamiento del cloud (por ejemplo, un blob storage).


  Yo tengo un programa que he creado usando la librería Spark.

  Ese programa lo voy a ejecutar en mi máquina local, pero lo lanzaré contra un cluster de Spark.

    
    MI MAQUINA                               CLUSTER SPARK
    +----------------+                   +------------------------------------------------------------+
     miPrograma.py     ------------------->   Maestro   ------------->      Nodo 1
                             *1                         ------------->      Nodo 2
                                                        ...
                                                        ------------->      Nodo N
    python miPrograma.py

    Y en mi máquina es 
    donde se abre un proceso 
    python que usa la librería Spark
    para conectarse al cluster.

    *1... Qué manda mi programa al cluster?
    - datos. Se mandan al maestro. Y el maestro los particiona y manda particiones de los datos (subconjuntos) a los nodos.
             Cada nodo recibe una o varias particiones de los datos, para que los procesen.
    - las operaciones que deben ejecutar los nodos sobre los datos.
             Esas operaciones las he definido como FUNCIONES en mi programa.
             Las funciones (lógica/código) Viajan por la red desde mi máquina al maestro, y el maestro las reenvía a los nodos.
             Todos los nodos reciben todas las funciones que deben ejecutar.
             Las funciones que he programado (de forma tradicional o mediante expresiones lambda) son tratadas como un DATO más, que viaja por la red.

# SPARK reparte datos... no tareas...
Todos los nodos ejecutan las mismas funciones (tareas), pero cada nodo lo hace sobre un conjunto diferente de datos (una partición de los datos totales).
Pero Spark no es la única tecnología que permite hacer procesamiento distribuido.

# STORM (Otro proyecto Apache)
Storm (del que no vamos a hablar en el curso y que se usa menos que Spark, mucho menos)... lo que hace es repartir TAREAS entre los nodos, no datos.

Storm pondría 1 nodo a hacer el doblado. A otro a hacer la división entre 3. A otro a hacer el redondeo. Y así sucesivamente.
Y los datos TODOS fluyen por todos los nodos.

Es otra estrategia diferente!

---

Volviendo a Spark.
Una pregunta muy habitual es en cuantos conjuntos particionar los datos.
Habitualmente parto el conjunto de datos en muchas más particiones que nodos/cores tengo en el cluster.
Voy a querer que cada nodo reciba ... tropetantas particiones.
¿Por qué?
- No sé la carga de trabajo que tiene cada nodo del cluster. 
  Mi app no será la única que se ejecuta en el cluster.
  Puede ser que un nodo esté ocupado con otras tareas.
  Y en paralelo que otro esté libre.
  Y lo que quiero es que si uno acaba rápido, pueda ir recibiendo más particiones de datos para procesar.
- Imaginad que mi partición de datos es muy grande.: 100.000 datos.
  Y el nodo se pone a procesar. ... y cuando va por el 99.999 el nodo se cae!
  Pierdo todo el trabajo que ha hecho el nodo.
  Spark se recupera.. mandará esos 100.000 datos a otro nodo para que los procese.
  Pero a empezar de 0!

Habitualmente preferimos hacer muchas más particiones de datos, y que cada partición sea más pequeña.
Aquí hay que llegar a una solución de compromiso, porque hay una característica.-
Con cada paquete de datos que envío a un nodo, también se envía la lógica (las funciones) que debe ejecutar el nodo.
Si mando 1 paquete con 1.000.000 de datos, mando 1 paquete de datos y 1 paquete con las funciones.
Si mando 1.000 paquetes con 1.000 datos, mando 1.000 paquetes de datos y 1.000 paquetes con las funciones.
Mando las funciones 1000 veces. Y eso me produce cierto overhead (sobrecarga) en la red.
Tampoco me vuelvo loco y hago particiones de 1 dato cada una.

Pero ... 100, 1000, 10000 particiones suele ser razonable.
Depende de el tipo de dato y el procesamiento que haga.
