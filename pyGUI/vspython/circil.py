from turtle import *
pen=Turtle()
def dico():
    pen.fillcolor("gray")
    pen.begin_fill()
#1
    pen.left(10)
    pen.pencolor("red")
    pen.fd(100)

    pen.right(245)
    pen.pencolor("blue")
    pen.fd(100)

    pen.left(80)
    pen.pencolor("green")
    pen.fd(100)

    pen.right(255)
    pen.pencolor("yellow")
    pen.fd(75)
#2
    pen.left(60)
    pen.pencolor("yellow")
    pen.fd(100)

    pen.right(245)
    pen.pencolor("green")
    pen.fd(100)

    pen.left(80)
    pen.pencolor("blue")
    pen.fd(100)

    pen.right(255)
    pen.pencolor("red")
    pen.fd(75)

#3
    pen.left(60)
    pen.pencolor("blue")
    pen.fd(100)

    pen.right(245)
    pen.pencolor("green")
    pen.fd(100)

    pen.left(80)
    pen.pencolor("red")
    pen.fd(100)

    pen.right(255)
    pen.pencolor("yellow")
    pen.fd(75)
    
    pen.end_fill()
dico()