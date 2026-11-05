from turtle import *
import math
import random

# Setup screen
screen = Screen()
screen.title("Hot and Cold Game")
screen.bgcolor("white")
screen.setup(width= 600 , height= 600)

#player
player = Turtle()
player.shape("turtle")
player.color("blue")
player.penup()

#hidden target location
target_x = random.randint(-280 , 280)
target_y = random.randint(-280 , 280)
target = (target_x , target_y) #tuple for the target location

#target turtle(incisible on screen)
target_marker = Turtle()
target_marker.shape("circle")
target_marker.color("green")
target_marker.penup()
target_marker.goto(target)
target_marker.hideturtle()

#show hints messages
msg = Turtle()
msg.hideturtle()
msg.penup()
msg.goto(0, 260)
msg.color("red")

#store last distance
last_distance = math.dist(player.pos() , target)

#game active flag
game_active = True

#check hot , cold or win
def check_distance():
    global last_distance , game_active
    if not game_active:
        return
    
    current_distance = math.dist(player.pos() , target)

    if current_distance < 15:
        msg.clear()
        msg.write("🎯 You found it!" , align = "center" , font = ("arial" , 20 , "bold"))
        target_marker.showturtle()
        game_active = False

    elif current_distance < last_distance:
        msg.clear()
        msg.write("🔥 Getting Hotter , keep moving!" , align = "center" , font = ("arial" , 20 , "bold"))
    else:
        msg.clear()
        msg.write("❄️ Getting colder...." , align = "center" , font = ("arial" , 20 , "bold"))
    last_distance = current_distance


def move_up():
    if game_active:
        player.setheading(90)
        player.forward(20)
        check_distance()

def move_down():
    if game_active:
        player.setheading(270)
        player.forward(20)
        check_distance()

def move_left():
    if game_active:
        player.setheading(180)
        player.forward(20)
        check_distance()


def move_right():
    if game_active:
        player.setheading(0)
        player.forward(20)
        check_distance()


#key binding
screen.listen()
screen.onkey(move_down , "Down")
screen.onkey(move_up , "Up")
screen.onkey(move_left , "Left")
screen.onkey(move_right , "Right")

msg.write("Move with arrow keys to find the hidden target!!" , align = "center" , font = ("arial" , 20))


done()


