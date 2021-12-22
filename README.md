# Challenge
___
## Introducción

Con el objetivo de modelar un concurso de preguntas y respuestas, la intención es diseñar
una solución que permita tener un banco de preguntas con diferentes opciones para una
única respuesta, además cada pregunta debe estar en una categoría o un grupos de
preguntas similares del mismo nivel, por cada ronda se deberá asignar un premio a conseguir,
las rondas del juego son nivel que van aumentando en la medida que el jugador gana premios.
___
## _Condiciones del concurso_

1. Precondiciones: Debe de tener 25 preguntas (5 preguntas por categorías) para 5
rondas, cada categoría tiene una complejidad o nivel de dificultad, cada ronda debe
asignarle un premio que el jugador va a ganar, el premio puede ser puntos o dinero.
2. El jugador inicia con la primera ronda, el sistema busca la categoría del primer nivel y
escoge una pregunta de esa categoría.
3. El Jugador selecciona una opción de las 4 opciones que tiene, si pierde se finaliza el
juego si gana continua a la siguiente ronda.
4. La siguiente ronda selecciona una pregunta de un grado de complejidad mayor según
la categoría. Hace el mismo comportamiento del ítem 4.
5. Si llega a la ronda 5 y pasa, entonces gana el juego, el premio mayor debería estar en
la última ronda.


## requisitos para correr el proyecto

El modelo está planteado para ejecutarse desde la consola de comandos.
Python Version 3 o superior para ejecutar el archivo main.py (python main.py)


> Nota: se utilizo 2 archivos .csv para el resguardo de datos 
> en ranking.csv se almacena los puntajes de usuarios con detalles.
> En questions.csv se almacena las preguntas utilizadas con sus 
opciones y detalle de correcta/incorrecta.  



[//]: #