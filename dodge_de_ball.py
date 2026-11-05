from turtle import *
import random
#screen setup
win = Screen() # To create a screen
win.title("Dodge the ball....")
win.bgcolor("white")
win.setup(width = 500, height = 600 )#height and width of screen
win.tracer(0) #do not auto update


#player
player = Turtle()
player.shape("square")
player.shapesize(stretch_wid=2.5, stretch_len=2.5)
player.color('blue')
player.penup()

#balls
balls = [] #empty list for balls
ball_speed = [6, 8, 10]

score = 0
game_over = False

#score Display
score_display = Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(-200, 260)
score_display.write("Score : 0 ", font = ("Arial", 15 , "bold"))

#move the player with mouse drag
def follow_mouse(x, y):
    player.goto(x, y)

#bind the mouse button
player.ondrag(follow_mouse)


#creating balls on screen
def create_ball():
    ball = Turtle()
    ball.shape("circle")
    ball.color("red")
    ball.penup()
    ball.goto(random.randint(-230, 230), 300)
    ball.speed_val = random.choice(ball_speed)
    balls.append(ball)


def game_loop():
    global score, game_over

    if not game_over:
        for ball in balls[:]:
            ball.sety(ball.ycor() - ball.speed_val)

            #remove ball off screen
            if ball.ycor() < -300:
                balls.remove(ball)
                ball.hideturtle()
                score += 1
                score_display.clear()
                score_display.write(f"Score : {score} ", font = ("Arial", 15 , "bold"))



            #ball colliding with player
            if player.distance(ball) < 30:
                game_over = True
                score_display.goto(0, 0)
                score_display.write("GAME OVER BLUD!!!!!", align = "center", font = ("Arial", 15 , "bold"))
        #spawn ball after a set interval of time
        if random.randint(1, 10) == 1:
            create_ball()
        
        win.update()
        win.ontimer(game_loop, 15)  #faster update
        


game_loop()






done()