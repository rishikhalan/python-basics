from turtle import *
from random import randint

speed(0)
bgcolor('skyblue')
penup()
goto(-200, 150)
#track     
for i in range(1, 16):
    write(i, align="center", font=("Times", 20))
    right(90)
    for num in range(15):
        penup()
        forward(10)
        pendown()
        forward(10)
    penup()
    back(300)
    left(90)
    forward(30)
hideturtle()

def make_turtle(y_position, color):
    t = Turtle()
    t.shape('turtle')
    t.turtlesize(2)
    t.color(color)
    t.penup()
    t.goto(-230, y_position)
    return t

t1 = make_turtle(100, 'red')
t2 = make_turtle(30, 'blue')
t3 = make_turtle(-40, 'green')
t4 = make_turtle(-110, 'navy')

winner = None


while True:
    t1.forward(randint(1, 5))
    t2.forward(randint(1, 5))
    t3.forward(randint(1, 5))
    t4.forward(randint(1, 5))

    if(t1.xcor() >= 250 or t2.xcor() >= 250 or t3.xcor() >= 250 or t4.xcor() >= 250 ):
        if winner is None:
            if t1.xcor() >= 250:
                winner = t1.pencolor()
            if t2.xcor() >= 250:
                winner = t2.pencolor()
            if t3.xcor() >= 250:
                winner = t3.pencolor()
            if t4.xcor() >= 250:
                winner = t4.pencolor()
        penup()
        goto(0, 200)
        pencolor(winner)
        write('Winner is : '+ winner.upper(), align = 'center', font = ('Comic Sans MS', 30, 'bold'))
        break

mainloop()