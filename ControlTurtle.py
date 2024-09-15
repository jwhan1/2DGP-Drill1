import turtle
turtle.shape("turtle")

arrow = input()
turtle.setheading(90)
#루프
def forwardmove():
    turtle.setheading(90)
def leftmove():
   turtle.setheading(180)
def backmove():
    turtle.setheading(270)
def rightmove():
    turtle.setheading(0)
def drawclear():
    turtle.home()
    turtle.clear()
    turtle.setheading(90)
while 1:
#방향전환 
    turtle.onkey(forwardmove,'w')
    turtle.onkey(leftmove,'a')
    turtle.onkey(backmove,'s')
    turtle.onkey(rightmove,'d')
    turtle.onkey(drawclear, 'Escape')
#전진하고 입력
    turtle.forward(50)
    turtle.stamp()
    turtle.listen()
