
import turtle
import time
def love():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)
time.sleep(1)
turtle.color('blue', 'pink')
turtle.pensize(2)
turtle.speed(10)
turtle.goto(0, 0)

turtle.begin_fill()
turtle.left(140)
turtle.forward(112)
love()
turtle.left(120)
love()
turtle.forward(112)
turtle.end_fill()
turtle.pensize(5)
turtle.up()
turtle.goto(-50, 142.7)
turtle.left(50)
turtle.down()
turtle.forward(60)
turtle.left(90)
turtle.forward(25)
turtle.up()
turtle.goto(37.5, 142.7)
turtle.down()
turtle.forward(25)
turtle.up()
turtle.goto(50, 142.7)
turtle.right(90)
turtle.down()
turtle.forward(60)
for i in range(20):
    turtle.right(7.8)
    turtle.forward(0.3)
turtle.forward(8)
turtle.up()
turtle.goto(100, -10)
turtle.write("I Love you")
time.sleep(4)




