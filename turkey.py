from turtle import * 
bgcolor("white")
speed(0)
pencolor("red")

fillcolor("red")
begin_fill()
for i in range(2):
    forward(250)
    right(90)
    forward(175)
    right(90)

end_fill()

penup()
goto(100, -125)
pendown()

fillcolor("white")
begin_fill()
circle(40)
end_fill()

penup()
goto(110, -119)
pendown()

fillcolor("red")

begin_fill()
circle(33)
end_fill()

penup()
goto(150, -90)
left(45)
pendown()

fillcolor("white")
begin_fill()
for i in range (5):
    forward(15)
    left(144)
    forward(15)
    right(72)
end_fill()


hideturtle()
mainloop()


