from turtle import *
bgcolor("skyblue")
pencolor("yellow")
fillcolor("yellow")
begin_fill()
for i in range (5):
    forward(100)
    left(144)
    forward(100)
    right(72)

end_fill()
penup()
goto(200, 200)

pendown()
pensize(10)

for i in range (5):
    forward(20)
    left(144)


penup()
goto(-200, -200)

pendown()
pensize(2)

for i in range(3):
    forward(60)
    left(120)

penup()
goto(-200, -165)

pendown()

for i in range(3):
    forward(60)
    right(120)


mainloop()