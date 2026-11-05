from turtle import * 
bgcolor("yellow")
speed(0)

fillcolor("skyblue")
begin_fill()
for i in range(4):
    forward(200)
    left(90)
end_fill()


penup()
goto(-200,-200)
pendown()
#triangle

fillcolor("skyblue")
begin_fill()
for i in range(3):
    forward(200)
    left(120)
end_fill()

penup()
goto(450,300)
pendown()
#hexagon

fillcolor("skyblue")
begin_fill()
for i in range(6):
    forward(50)
    left(60)
end_fill()

penup()
#circle
pencolor("skyblue")
pensize(7)
goto(450,-300)
pendown()
fillcolor("black")
begin_fill()
for i in range(360):
    forward(1)
    left(1)
end_fill()

penup()
goto(200,200)
pendown()
write("SPEED",align="center",font=("Comic Sans MS",50 ))
#cresent
penup()
goto(-300,300)
pendown()
pencolor("white")
fillcolor("white")
begin_fill()
circle(70)
end_fill() 



penup()
goto(-260,300)
pendown()
pencolor("yellow")
fillcolor("yellow")
begin_fill()
circle(70)
end_fill() 






hideturtle()
mainloop()