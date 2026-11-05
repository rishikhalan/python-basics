from turtle import * 
bgcolor("sky blue")
speed(0)

#Germany
fillcolor("yellow")
begin_fill()

forward(200)
right(90)
forward(40)
right(90)
forward(200)
right(90)
forward(40)
right(90)

end_fill()

left(90)

fillcolor("red")

begin_fill()

forward(40)
right(90)
forward(200)
right(90)
forward(40)
right(90)
forward(200)
right(90)

end_fill()

fillcolor("black")

begin_fill()

forward(40)
forward(40)
right(90)
forward(200)
right(90)
forward(40)
right(90)
forward(200)
right(90)

end_fill()

penup()
goto(-300, 200)
pendown()
fillcolor("dark blue")
begin_fill()
forward(200)
right(90)
forward(50)
right(90)
forward(200)
right(90)
forward(50)
right(180)
end_fill()


penup()
forward(50)
pendown()
fillcolor("white")
begin_fill()
forward(50)
left(90)
forward(200)
left(90)
forward(50)
left(90)
forward(200)
left(90)
end_fill()



penup()
forward(50)
pendown()
fillcolor("red")
begin_fill()
forward(50)
left(90)
forward(200)
left(90)
forward(50)
left(90)
forward(200)
left(90)

end_fill()



mainloop()