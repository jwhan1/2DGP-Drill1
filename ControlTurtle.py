import turtle
turtle.shape("turtle")

#루프
def forwardmove():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()
def leftmove():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()
def backmove():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()
def rightmove():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()
def drawclear():
    turtle.home()
    turtle.clear()

#방향전환 
turtle.onkey(forwardmove,"w")
turtle.onkey(leftmove,"a")
turtle.onkey(backmove,"s")
turtle.onkey(rightmove,"d")
turtle.onkey(drawclear, "Escape")
#전진하고 입력

turtle.listen()
