from turtle import * 
bgcolor("white")
speed(0)

fillcolor("darkblue")
begin_fill()

#north korea
forward(200)
left(90)
forward(30)
left(90)
forward(200)
left(90)
forward(30)
end_fill()

fillcolor("white")
begin_fill()

forward(10)
left(90)
forward(200)
left(90)
forward(10)
left(90)
forward(200)
left(90)
end_fill()

penup()
forward(10)
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

penup()
forward(50)
pendown()

fillcolor("white")
begin_fill()

left(90)
forward(200)
left(90)
forward(10)
left(90)

forward(200)
left(90)
forward(10)
left(90)
end_fill()



#for star coordinates are x=50 and y=65???


fillcolor("darkblue")
begin_fill()

right(90)
forward(30)
left(90)
forward(200)
left(90)
forward(30)
left(90)
forward(200)
end_fill()


penup()
goto(100,-10)
pendown()

fillcolor("white")
begin_fill()


circle(20)

end_fill()




penup()
goto(97,-23)
pendown()

fillcolor("red")
begin_fill()

for i in range (5):
    forward(10)
    left(144)
    forward(10)
    right(72)
end_fill()


hideturtle()
mainloop()