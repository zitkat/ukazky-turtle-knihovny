
import turtle
import random
import datetime

from ucastnici import jmena

wn = turtle.Screen()
wn.bgcolor("dimgray")
t = turtle.Turtle()
t.hideturtle()
t.pensize(3)
t.speed(0)

barvy = ["black", "navy", "darkslategrey"]
fs = 18 # font size

t.pu()
t.goto(-150, 150)
t.pd()


for ii in range(40):
        t.pencolor(random.choice(barvy))
        t.penup()
        t.fd(1)
        t.pd()
        t.write( "python", align="center", font=("Arial", fs + 2 * ii, "bold") )
        t.left(90)


t.pu()
t.goto(-140, -20)
t.pd()

dnes = datetime.datetime.now()

msg = "\n".join(["Zdravíčko!", 
                dnes.strftime("Dnes je: %A, %d. %B, %Y") , 
                dnes.strftime("Hodin je: %H:%M") ,
                dnes.strftime("Den v roce: %j") ,
                dnes.strftime("Týden v roce: %U")])

t.color("black")
t.write( msg, font=('Arial', 18 , 'bold'), align='center')

t.pu()
t.goto(-120, -80)
t.pd()


jmena.sort()

t.up()
t.write("Zdraví:", font=("Arial", 14, "normal"))
#t.fd(80)
t.setheading(-90)
for jmeno in jmena:
        t.goto(random.randint(50, 200), random.randint(-100, 0))
        t.write("%s" % jmeno, font=("Arial", 12, "normal"), align="center")
        #t.forward(15)
        
wn.exitonclick()