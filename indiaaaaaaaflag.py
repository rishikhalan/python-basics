from turtle import *


speed(0)

bgcolor('lightblue')
penup()
goto(-300, 250)
fillcolor('#ffa838')
begin_fill()

for i in range(2):
    forward(600)
    right(90)
    forward(150)
    right(90)
end_fill()
#white
right(90)
forward(150)
left(90)
fillcolor('white')
begin_fill()

for i in range(2):
    forward(600)
    right(90)
    forward(150)
    right(90)
end_fill()
#green
right(90)
forward(150)
left(90)
fillcolor('green')
begin_fill()

for i in range(2):
    forward(600)
    right(90)
    forward(150)
    right(90)
end_fill()

goto(0, -30)

pendown()
pencolor('navy')
pensize(7)
circle(54)
penup()


goto(-6, -25)
fillcolor('navy')


for i in range(25):
    begin_fill()
    circle(1)
    end_fill()
    penup()
    forward(13)
    left(360/24)
    pendown()

penup()

goto(0,25)
pendown()
pensize(2)

for i in range(24):
    forward(40)
    back(40)
    left(360/24)

hideturtle()

mainloop()