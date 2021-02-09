
import turtle
import random

wn = turtle.Screen()
wn.bgcolor("dimgray")
t = turtle.Turtle()
t.hideturtle()

#wn.register_shape("img/python.gif")

class Hrac(turtle.Turtle):
    def __init__(self, tvar, barva):
        turtle.Turtle.__init__(self, shape=tvar)
        self.penup()
        self.speed = 1 
    
    def doleva(self):
        self.left(45)
    
    def doprava(self):
        self.right(45)
    
    def urychlit(self):
        self.speed += 1
    
    def zpomalit(self):
        self.speed -= 1

    def pohyb(self): 
        self.fd(self.speed)

class Ostatni(turtle.Turtle):
    def __init__(self, tvar, barva, x, y):
        turtle.Turtle.__init__(self, shape=tvar)
        self.penup()
        self.speed = 1
        self.color(barva)
        self.setheading( random.randint(0, 360) )
        self.x = x 
        self.y = y
  
    def pohyb(self): 
        self.fd(self.speed)


hrac = Hrac("arrow", "black")
ostatni = Ostatni("circle", "pink", 150, 50)
#ostatni = Ostatni("img/python.gif", "pink", 150, 50)

wn.listen()
wn.onkeypress(hrac.doleva, "Left")
wn.onkeypress(hrac.doprava, "Right")
wn.onkeypress(hrac.urychlit, "Up")
wn.onkeypress(hrac.zpomalit, "Down")

while True:
    hrac.pohyb()
    ostatni.pohyb()



