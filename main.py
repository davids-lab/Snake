from turtle import Screen, Turtle
import time
from serpientes import Serpientes
from comida import Comida
from puntaje import Puntaje

pantalla = Screen()
pantalla.setup(width=600, height=600)
pantalla.bgcolor("black")
pantalla.title("Juego Snake en Python")
pantalla.tracer(0)

serpiente = Serpientes()
comida = Comida()
puntaje = Puntaje()

pantalla.listen()
pantalla.onkey(serpiente.arriba, "Up")
pantalla.onkey(serpiente.abajo, "Down")
pantalla.onkey(serpiente.izquierda, "Left")
pantalla.onkey(serpiente.derecha, "Right")


juego_encendido = True

while juego_encendido:
    pantalla.update()
    time.sleep(0.1)
    serpiente.movimiento()

    #Detectar contacto con la comida
    if serpiente.head.distance(comida) < 15:
        comida.refrescar()
        serpiente.extender()
        puntaje.mostrar_puntaje()

    #Detectar contacto con paredes (Game over)
    if serpiente.head.xcor() > 290 or serpiente.head.xcor() < -290 or serpiente.head.ycor() > 290 or serpiente.head.ycor() < -290:
        juego_encendido = False
        puntaje.juego_terminado()

    #Detectar colision con si misma (Game over)
    for segmento in serpiente.segmentos[1:]:
        if serpiente.head.distance(segmento) < 10:
            juego_encendido = False
            puntaje.juego_terminado()



pantalla.exitonclick()