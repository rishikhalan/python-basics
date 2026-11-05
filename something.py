from turtle import * 
speed(0)
win = Screen()
win.setup(width=800, height=500)
colormode(255)
r, g, b = 0, 0, 255
for i in range(50):
    fillcolor(r, g, b)
    begin_fill()
    penup()
    goto(-400 , -250+(i * 12))
    forward(1200)
    left(90)
    forward(12)
    left(90)
    forward(1200)
    left(90)
    forward(12)
    left(90)
    end_fill()
    b -= 5


def square(size, color):
    fillcolor(color)
    begin_fill()
    for i in range(4):
        forward(size)
        right(90)
    end_fill()

def triangle(size, color):
    fillcolor(color)
    begin_fill()
    for i in range(3):
        forward(size)
        left(120)
    end_fill()

def rectangle(l, w, color):
    fillcolor(color)
    begin_fill()
    for i in range(2):
        forward(l)
        right(90)
        forward(w)
        right(90)
    end_fill()

#grass

penup()
goto(-400, -150)
rectangle(800, 100, "#065109")

#house

goto(-300, -50)
square(100, "#FBCB0B")



#roof
triangle(100, "#C17605")


#door


goto(-265, -90)
rectangle(30, 60, "#5F3C00")


#doorknob
goto(-245, -120)
fillcolor('yellow')
begin_fill()
circle(5)
end_fill()


#windows r

goto(-230, -60)
square(15,"#04DFFC")


#windows llll

goto(-285, -60)
square(15,"#04DFFC")


#car

goto(-100, -75)
rectangle(150, 50, "#F10707")

goto(-75, -25)
rectangle(85, 50, "#F10707")

#cwindows
goto(-75, -36)
rectangle(30, 30 , "#89E8EE")

goto(-20, -36)
rectangle(30, 30 , "#89E8EE")


#wheellllsss lefftt
goto(-70, -155)
fillcolor('black')
begin_fill()
circle(25)
end_fill()



#wheellllsss right
goto(15, -155)
fillcolor('black')
begin_fill()
circle(25)
end_fill()


#tree
goto(170, -80)
rectangle(30, 70, "#76450E")
y = -80
for i in range(3):
    goto(140, y)
    triangle(90, "#26630C")
    y+=40



#Cresenct
goto(250, 150)

fillcolor("#E9DEA2")
begin_fill()
circle(40)
end_fill()

goto(270, 160)

fillcolor("#030845")
begin_fill()
circle(40)
end_fill()



hideturtle()
mainloop()

