from turtle import Turtle

ALINEACION = "center"
FUENTE = ("Arial", 13, "normal")

class Puntaje(Turtle):
    def __init__(self):
        super().__init__()
        self.puntaje = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.actualizar_puntaje()

    def actualizar_puntaje(self):
        self.write(f"Puntos: {self.puntaje}", align=ALINEACION, font=FUENTE)

    def mostrar_puntaje(self):
        self.clear()
        self.puntaje += 1
        self.actualizar_puntaje()

    def juego_terminado(self):
        self.goto(0,0)
        self.write("JUEGO TERMINADO", align=ALINEACION, font=FUENTE)