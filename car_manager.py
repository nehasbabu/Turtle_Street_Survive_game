import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
class CarManager():
    def __init__(self):
        super().__init__()
        self.care=[]
        self.sp=STARTING_MOVE_DISTANCE
    def car(self):
        r=random.randint(1,6)
        if r==1:
            newcar=Turtle("square")
            newcar.penup()
            newcar.shapesize(1,2)
            newcar.color(random.choice(COLORS))
            newcar.goto(300,random.randint(-250,250))
            self.care.append(newcar)
    def movement(self):
        for car in self.care:
            car.backward(self.sp)
    def speedup(self):
        self.sp+=MOVE_INCREMENT

