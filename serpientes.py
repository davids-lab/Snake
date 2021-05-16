from turtle import Turtle
import time

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
DISTANCIA_MOVIMIENTO = 20
ARRIBA = 90
ABAJO = 270
IZQUIERDA = 180
DERECHA = 0

segmentos = []


class Serpientes:
    def __init__(self):
        self.segmentos = []
        self.crear_serpiente()
        self.head = self.segmentos[0]


    def crear_serpiente(self):
        for posicion in STARTING_POSITIONS:
            self.agregar_segmento(posicion)


    def agregar_segmento(self, posicion):
        nuevo_segmento = Turtle("square")
        nuevo_segmento.color("white")
        nuevo_segmento.penup()
        nuevo_segmento.goto(posicion)
        self.segmentos.append(nuevo_segmento)

    def extender(self):
        #Agregar nuevo segmento a la serpiente cuando coma
        self.agregar_segmento(self.segmentos[-1].position())


    def movimiento(self):
        for nro_segmento in range(len(self.segmentos) - 1, 0, -1):
            new_x = self.segmentos[nro_segmento - 1].xcor()
            new_y = self.segmentos[nro_segmento - 1].ycor()
            self.segmentos[nro_segmento].goto(new_x, new_y)
        self.head.forward(DISTANCIA_MOVIMIENTO)


    def arriba(self):
        if self.head.heading() != ABAJO:
            self.head.setheading(ARRIBA)

    def abajo(self):
        if self.head.heading() != ARRIBA:
            self.head.setheading(ABAJO)

    def izquierda(self):
        if self.head.heading() != DERECHA:
            self.head.setheading(IZQUIERDA)

    def derecha(self):
        if self.head.heading() != IZQUIERDA:
            self.head.setheading(DERECHA)

