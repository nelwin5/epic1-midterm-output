#Nelwin Serra BSCS 1B
#"Petals of Pleasures"

import turtle
turtle.speed(20)
sc=turtle.Screen()
sc.bgcolor("black")
sc.title("Petals of Pleasures")

def pen(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def pattern1():
    turtle.pensize(4)
    for i in range(50):
        if i < 10:
            turtle.pencolor('gold')
        elif i <= 20:
            turtle.pencolor('orange')
        elif i <= 30:
            turtle.pencolor('dark orange')
        elif i <= 40:
            turtle.pencolor('chocolate')
        else:
            turtle.pencolor('yellow')
        turtle.circle(190+1, 90)
        turtle.lt(98)
        turtle.circle(190-1, 90)
        turtle.lt(18) 

def circle(psize, csize, color):
    turtle.pensize(psize)
    turtle.pencolor(color)
    turtle.circle(csize)

def pattern2():
    turtle.pensize(2)
    turtle.pencolor('saddle brown')
    for i in range(180):
        turtle.forward(8.5)
        turtle.left(2)
        turtle.circle(20)

def pattern3(r, l, f, csize, psize):
    for i in range(r):
        turtle.color('dark green')
        turtle.pencolor('lime green')
        turtle.pensize(psize)
        turtle.penup()
        turtle.left(l)
        turtle.forward(f)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(csize)
        turtle.end_fill()

def pattern4(r, l, f, csize, color, psize):
    turtle.pencolor(color)
    for i in range(r):
        turtle.pensize(psize)
        turtle.penup()
        turtle.left(l)
        turtle.forward(f)
        turtle.pendown()
        turtle.circle(csize)

def pattern5(radius):
    turtle.pensize(3)
    for i in range (10):
        if i < 2:
            turtle.pencolor('red')
        elif i <= 4:
            turtle.pencolor('crimson')
        elif i <= 6:
            turtle.pencolor('magenta')
        elif i <= 8:
            turtle.pencolor('hot pink')
        else:
            turtle.pencolor('navajo white')
        turtle.circle(radius)
        radius=radius-4

def pattern6():
    for i in range (10):
        pattern5(85)
        turtle.right(36)


turtle.up()
turtle.pencolor('black')
pen(1000,0)
turtle.backward(2000)
pen(0,1000)
turtle.right(90)
turtle.forward(2000)
turtle.down()

pen(35,-3.7)
pattern1()

pen(-186,-157)
circle(20, 244, 'black')

turtle.color('black')
turtle.begin_fill()
pen(-158,-133)
circle(9, 207, 'black')
turtle.end_fill()

pen(0,0)
pattern6()

pen(-189, -154)
pattern2()

pen(-140, -131)
pattern3(60, 6 , 20, 7, 2)

pen(-206, -201)
pattern4(45, 8 , 40, 5, 'white', 3)

turtle.hideturtle()
turtle.exitonclick()

