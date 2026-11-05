from turtle import *
speed(0)
bgcolor('black')
colors = ['green', 'red', 'yellow', 'blue', 'coral']
pensize(2)
for i in range(30):
    for color in colors:
        pencolor(color)
        circle(120)
        left(360/ 150)

mainloop()