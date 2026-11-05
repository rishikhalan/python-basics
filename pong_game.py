from turtle import *

#screen setup
win = Screen() #to create a screen
win.title("Pong game")
win.bgcolor("white")
win.setup(width = 600 , height = 600) #height and width of screen
win.tracer(0) #do not auto update

#player
player = Turtle()
player.shape("square")
player.shapesize(stretch_wid=1 , stretch_len=6)
player.color("black")
player.penup()
player.goto(0 , -250)

#Ball
ball = Turtle()
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0 , 0)

#ball Speed
dx = 3 #horizontal speed -- speed_x
dy = 3 #verticla speed -- speed_y

#bricks
colors = ["red", "orange", "gold", "lime", "cyan"]
bricks = []
ystart = 250

for row in range(5):
    for column in range(-250, 260, 60):
        brick = Turtle()
        brick.shape("square")
        brick.shapesize(stretch_wid=1, stretch_len=2.5)
        brick.color(colors[row])
        brick.penup()
        brick.goto(column, ystart - (row * 30))
        bricks.append(brick)

#Paddle movement
def p_left():
    x = player.xcor() - 70
    if x < -250:
        x = -250
    player.setx(x)

def p_right():
    x = player.xcor() + 70
    if x > 250:
        x = 250
    player.setx(x)

win.listen()
win.onkey(p_left, "Left")
win.onkey(p_right, "Right")

#ball movement
def b_move():
    global dx, dy
    x, y = ball.xcor(), ball.ycor()

    #ball bounce on walls
    if x + dx > 290 or x + dx < -290:#left and right wall
        dx = -dx
    if y + dy> 290: #top wall
        dy = -dy

    #ball bounce on paddle
    if ball.distance(player) < 50 and y + dy < -230:
        dy = -dy
    
    #ball collision with bricks
    for brick in bricks:
        if brick.distance(ball) < 30:
            dy = -dy
            if brick.goto(1000, 1000):
                bricks.remove(brick)
            break
    

    #Game over
    if y + dy < -290:
        ball.hideturtle()
        game_over = Turtle()
        game_over.color("red")
        game_over.hideturtle()
        game_over.write("~~ Game Over ~~", align = "center", font = ("arial", 50, "bold"))
        win.update()
        return
    
    #move ball
    ball.goto(x + dx, y + dy)


    #GAME WIN
    if not bricks:
        ball.hideturtle()
        win_turtle = Turtle()
        win_turtle.color("red")
        win_turtle.hideturtle()
        win_turtle.write("~~ Game Over ~~", align = "center", font = ("arial", 50, "bold"))
        win.update()
        return
    
    win.update()
    win.ontimer(b_move, 10)

win.update()
b_move()

done()

