
import turtle
import random

wn = turtle.Screen()
wn.bgcolor("dimgray")
t = turtle.Turtle()
t.hideturtle()
t.pensize(2)
t.shape("circle")

# def kresliNaKlik(x, y):
#     t.goto(x, y)
#     t.dot()

def kresliNaKlik(x, y):
    t.goto(x, y)
    for i in range( random.randint(8, 100) ):
        t.forward(i)
        t.dot()
        t.left(50)

wn.onclick(kresliNaKlik)

wn.mainloop()

