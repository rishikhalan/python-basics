from turtle import * 
bgcolor("white")
speed(0)

fillcolor("white")
begin_fill()

for i in range(2):
    forward(250)
    right(90)
    forward(20)
    right(90)


end_fill()
right(90)
penup()
forward(20)
pendown()
begin_fill()
fillcolor('blue')

right(270)

for i in range (2):
    forward(250)
    right(90)
    forward(30)
    right(90)

end_fill()
right(90)
forward(30)
right(270)
begin_fill()
fillcolor('white')

for i in range (2):
    forward(250)
    right(90)
    forward(75)
    right(90)

#------------------------------------------------------------------


end_fill()
right(90)
penup()
forward(75)
pendown()
begin_fill()
fillcolor('blue')

right(270)

for i in range (2):
    forward(250)
    right(90)
    forward(30)
    right(90)

end_fill()
right(90)
forward(30)
right(270)
begin_fill()
fillcolor('white')

for i in range(2):
    forward(250)
    right(90)
    forward(20)
    right(90)


penup()
goto(100, -71)
pendown()
pencolor("blue")
pensize(5)
for i in range(3):
    forward(55)
    right(120)

penup()
goto(100, -106)
pendown()

for i in range(3):
    forward(55)
    left(120)



hideturtle()
mainloop()

