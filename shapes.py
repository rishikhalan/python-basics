from turtle import *
speed(0)
def shape(colors, size, sides):
    fillcolor(colors)
    begin_fill()
    angle = 360 / sides
    for i in range(sides):
        forward(size)
        right(angle)
    end_fill()
    mainloop()
# main programmmm
colors = input('enter de color: ')
size = int(input('enter de size: '))
sides = int(input('enter de num of sides: '))

shape(colors, size, sides)


