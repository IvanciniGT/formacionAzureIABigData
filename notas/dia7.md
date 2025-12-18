

Clasificación de imágenes con Azure Cognitive Services
===================================================================

Imágenes de plantas de cicuta
Imágenes de plantas del cerezo japonés

Le vamos a dar un montón de imágenes de ambas... ya clasificadas.
- Con la etiqueta cerezo 10 fotos o 200
- Con la etiqueta cicuta 10 fotos o 200
NO SE ME OYE VERDAD????
Esto no entrena un modelo desde 0. Se usa el concepto de transferencia de aprendizaje.

Tomamos una red que tiene ya un montón de conocimiento sobre imágenes y la adaptamos a nuestro problema concreto.

Esa red ya sabe identificar formas, colores, texturas.... y así cientos de características visuales.

Entrenamos 1 neurona más en la última capa para que aprenda a distinguir entre cerezo y cicuta.

En este caso es un modelo de clasificación binaria... pero podría ser multiclase.
Es lo mismo.. cambia el tipo de función de activación de la última capa: softmax en lugar de sigmoide.

80-90-95 <- Razonablemente sencillo.. si hay datos.
---

Podría ser que nuestras imágenes tengan muchas etiquetas. Por ejemplo: 
- Cerezo, Mar, día
- Cerezo, montaña, noche
- Cicuta, campo, día
- Cicuta, mar, noche

La respuesta del modelo no es una etiqueta, sino un conjunto de etiquetas.

Esto cambia la forma en la que AZURE monta la última capa. 
Lo que monta no es una neurona por clase, sino una neurona por etiqueta.
Y cada neurona se activa o no de forma independiente.

---

# Cómo medimos si el modelo funciona bien o no?

Depende del problema.
- Falso positivo
- Falso negativo

Normalmente vereéis en estos modelos una medida de qué tal han ido llamada F1 Score.
Eso es una medida generalista que combina precisión y recall en un solo número.

A su vez:
- Precisión: De todas las veces que el modelo ha dicho "que la imagen es de un tipo", cuntas veces aácertó.
- Recall: De todas las veces que la imagen era de un tipo, cuántas veces el modelo lo detectó.

Y estos conceptos se desglosan con más detalle en lo que llamamos matriz de confusión.

50 fotos de cerezo y 50 de cicuta.

    MATRIZ DE CONFUSIÓN
|                | Predijo cerezo | Predijo cicuta |
|----------------|----------------|----------------|
| Es cerezo      |      45        |      5         |
| Es cicuta      |      10        |      40        |

El modelo ha dicho que cerezo son 45 + 10 = 55 fotos.
El modelo ha dicho que cicuta son 5 + 40 = 45 fotos.

De esas 55 fotos que el modelo dijo que eran cerezo, 45 eran realmente cerezo. -> %=81.8% precisión.
Se equivocó en 10 fotos que eran cicuta y dijo que eran cerezo -> Falso positivo. -> %=18.2% error.
De esas 45 fotos que el modelo dijo que eran cicuta, 40 eran realmente cicuta. -> %=88.8% precisión.
Se equivocó en 5 fotos que eran cerezo y dijo que eran cicuta -> Falso negativo. -> %=11.1% error.

Otra cosa es el recall.
De las 50 fotos que realmente eran cerezo, el modelo acertó 45. -> %=90% recall.
De las 50 fotos que realmente eran cicuta, el modelo acertó 40. -> %=80% recall.

De esos datos se calculan unos globales (medias ponderadas) que dan lugar al F1 Score.
F1 Score = 2 * (precisión * recall) / (precisión + recall)
En este caso:
F1 Score cerezo = 2 * (0.818 * 0.9) / (0.818 + 0.9) = 0.857
F1 Score cicuta = 2 * (0.888 * 0.8) / (0.888 + 0.8) = 0.842
F1 Score global = (0.857 + 0.842) / 2 = 0.8495      

---
Overfitting: Sobreajuste
Cuando el modelo aprende demasiado bien los datos de entrenamiento y no es capaz de llevar ese conocimieento a datos nuevos.

Cuando tengo pocos datos corro mucho este riesgo.

Imaginad que me dan en una empresa los datos de todos los empleados:

Numero de empleado,dni, nombre, apellidos, edad, departamento, años en la empresa, formación recibida, número de hijos, experiencia previa... coche que tiene... ---> salario


---

Me pasan una foto y quiero saber si hay un coche accidentado o no.
Y ese modelo lo estoy aplicando sobre cada 1000 fotogramas de un vídeo, que estoy captando en tiempo real.