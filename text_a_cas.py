
import turtle
import random
import datetime

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

msg = "Zdravíčko!\nDnes je: " + dnes.strftime("%A") + ', ' + dnes.strftime("%d") \
        + '. ' + dnes.strftime("%B") + ', ' + dnes.strftime("%Y") + \
        "\nHodin je: " + dnes.strftime("%H") + ':' + dnes.strftime("%M") + \
        "\nDen v roce: " + dnes.strftime("%j") + '\nTýden v roce: ' + dnes.strftime("%U")

t.color("black")
t.write( msg, font=('Arial', 18 , 'bold'), align='center')

t.pu()
t.goto(-140, -80)
t.pd()

jmena = ["ada", "eva", "tom", "míša", "mintaka"]
jmena.sort()

for i in jmena:
        t.write("\nzdraví: \n%s" % jmena, font=("Arial", 10, "normal"), align="center")
        
wn.exitonclick()