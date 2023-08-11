from turtle import *

pen=Turtle()
# for curve
def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

# heart
def heart():
    pen.fillcolor("red")

    pen.begin_fill()

    pen.left(130)
    pen.forward(150)

    curve()
    pen.left(140)

    curve()

    pen.right(0)
    pen.forward(150)

    pen.end_fill()
heart()
