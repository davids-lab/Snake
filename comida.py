from turtle import Turtle
import random

class Comida(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("coral")
        self.speed("fastest")
        self.refrescar()


    def refrescar(self):
        x_aleatoreo = random.randint(-250, 250)
        y_aleatoreo = random.randint(-250, 250)
        self.goto(x=x_aleatoreo, y=y_aleatoreo)