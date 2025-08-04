from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level=1
        self.levele()
    def gme(self):
        self.goto(0,0)
        self.write("GAME OVER",False,"center",FONT)
    def levelup(self):
        self.level+=1
        self.levele()
    def levele(self):
        self.clear()
        self.goto(-260,260)
        self.write(f"LEVEL : {self.level}", False, "center", ("Courier", 10, "normal"))

