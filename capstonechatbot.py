from turtle import *
import random
import math

#ball Speed
dx = 3 #horizontal speed -- speed_x
dy = 3 #vertical speed -- speed_y
#Above is for pong game
#-------------------------------------------------Calculator-----------------------------------------------
def calc():
    num=int(input("Give me a number: "))
    num_2=int(input("Give me a number: "))
    op=input("Give me a operator(+, -, *, /): ")
    if op == "*":
        print(f"{num} * {num_2} = {num * num_2}")

    elif op == "+":
        print(f"{num} + {num_2} = {num + num_2}")

    elif op == "-":
        print(f"{num} - {num_2} = {num - num_2}")

    elif op == '/':
        print(f"{num} / {num_2} = {num / num_2}")
    else:
        print("Invalid operator.")


#---------------------------------------------------QUIZ---------------------------------------------------------
def quiz() :
    quiz_score = 0
    print(" ~~ Capitals ~~ ")
    #QUES 1
    print("What is the capital of India? ")
    print("1. New Delhi")
    print("2. Kolkata")
    print("3. Mumbai")
    print("4. Bangalore")

    ans = int(input("Enter you answer (1-4): "))
    if ans == 1:
        quiz_score += 10
        print("\nGreat , that is the right answer !! .. You get 10 points")
    else:
        print("\nSorry, that is not right")

    # ------ QUES 2
    print("\nWhat is the capital of USA? ")
    print("1. Florida")
    print("2. California")
    print("3. New York")
    print("4. Washington DC")

    ans = int(input("Enter you answer (1-4): "))
    if ans == 4:
        quiz_score += 10
        print("\nGreat , that is the right answer !!  .. You get 10 points")
    else:
        print("\nSorry, that is not right")

    # ------ QUES 3
    print("\nWhat is the capital of Vietnam? ")
    print("1. Kuala Lumpur(KL)")
    print("2. Jakarta")
    print("3. Hanoi")
    print("4. I dunno")

    ans = int(input("Enter you answer (1-4): "))
    if ans == 3:
        quiz_score += 10
        print("\nGreat , that is the right answer !! .. You get 10 points")
    else:
        print("\nSorry, that is not right")



    print(f"I hope you enjoyed the quiz. Your total score is {quiz_score}.")



#-------------------------------------------Jokes----------------------------------------------------
def jokes():
    joke1 = ("What has a bed that you can’t sleep in? A river.🚣🛌")
    joke2 = ("How does the ocean say hello? It waves.🐬🏄👋")
    joke3 = ("Why couldn’t the leopard play hide and seek? Because he was always spotted.🐆🐆")
    jokes = [joke1, joke2, joke3]
    randon = random.choice(jokes)
    print(randon)
#---------------------------------------BMI Calculator-----------------------------------------------
def BMICalc():
    w=float(input("Give me your weight(kg): "))
    h=float(input("Give me your height (meters): "))
    bmi=w / (h*h)
    print(f"Your BMI(Body Mass Index) is: {bmi}")
    if bmi<18.5:
        print("You are underweight.")
    elif bmi>=18.5 and bmi<=24.9:
        print("Good job, you are a normal healthy person 👌😊😎")
    elif bmi>=25 and bmi<=29:
        print("You are overweight")
    elif bmi>=30 and bmi<=39.9:
        print("You are really overweight, please cut down on junk food.🍟🍕❌")
    else:
        print("You are a morbidly obese person.")


#---------------------------------------------Rock Paper Scissors----------------------------------------------------
def rps():
    print("🎮 Best of 3: Rock Paper Scissors")

    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0

    while player_score < 2 and computer_score < 2:
        player = input("\nEnter rock, paper, or scissors: ").lower()

        computer = random.choice(choices)
        print("Computer chose:", computer)

        # Check winner
        if player == computer:
            print("It's a tie!")
        elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score → You: {player_score}  Computer: {computer_score}")
    
    # Final Winner
    print("\n🏆 Final Result:")
    if player_score == 2:
        print("🎉 You win the match!")
    else:
        print("💻 Computer wins the match!")
#------------------------------------------Guess the number-------------------------------------------------------------
def guessnum():
    print('this is guess the number game.')
    snum=random.randint(1, 100)
    a=0
    while a<=10:
        g = int(input('give me ur guess: '))
        a = a+1
        if g == snum:
            print('You got it!')
            break
        elif g<snum:
            print('higher')
        elif g>snum:
            print('lower')
    if a > 10:
        ('You failed it was',snum)



#-------------------------------------Flags------------------------------------------------------------------------------------------------
def flags():
    speed(0)

    bgcolor('lightblue')
    penup()
    goto(-300, 250)
    
    #orange
    fillcolor('#ffa838')
    begin_fill()

    for i in range(2):
        forward(600)
        right(90)
        forward(150)
        right(90)
    end_fill()
    
    
    #white
    right(90)
    forward(150)
    left(90)
    fillcolor('white')
    begin_fill()

    for i in range(2):
        forward(600)
        right(90)
        forward(150)
        right(90)
    end_fill()
    
    
    #green
    right(90)
    forward(150)
    left(90)
    fillcolor('green')
    begin_fill()

    for i in range(2):
        forward(600)
        right(90)
        forward(150)
        right(90)
    end_fill()

    goto(0, -30)

    pendown()
    pencolor('navy')
    pensize(7)
    circle(54)
    penup()


    goto(-6, -25)
    fillcolor('navy')


    for i in range(25):
        begin_fill()
        circle(1)
        end_fill()
        penup()
        forward(13)
        left(360/24)
        pendown()

    penup()

    goto(0,25)
    pendown()
    pensize(2)

    for i in range(24):
        forward(40)
        back(40)
        left(360/24)

    hideturtle()

    mainloop()





#-------------------------------------dodge ball--------------------------------------------------------------------------------
#for dodge ball
score = 0
game_over = False


def dodgeball():
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
    ball_speed = [6, 4, 2]



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
            win.ontimer(game_loop, 10)  #faster update
            


    game_loop()
    mainloop()

#--------------------------------------------------------PONGGAME/Brick Breaker--------------------------------------------------------------------
def ponggame():
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

#-------------------------------------TurtlePattern-------------------------------
def Turtlepattern():
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

#For target game

last_distance = 0
#game active flag
game_active = True
#----------------------Target Game-------------------
def hotandcold():
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


#----------------------Alien Situation------------------
def alien_stuff():
    shield = input("You are the captain of a spaceship, and an alien ship approaches. Is your shield up? (All questions are y/n) ")
    if shield == 'y':
        laser = input('Is your laser charged? ')
        if laser == 'y':
            print("You attack first and win.")
        else:
            print("Alien attacks and damages you. ")
            flee = input('Do you try to flee? ')
            if flee == 'y':
                speed = int(input("What is your speed?(A number from 50 - 150 please) "))
                if speed > 80:
                    print('You escape!')
                else:
                    print('You’re caught.')
            else:
                print("'Instantly defeated you are', says Yoda, whilst coming out of the ship. ")
    else:
        flee = input('Do you try to flee? ')
        if flee == 'y':
            speed = int(input("What is your speed?(A number please) "))
            if speed > 80:
                print('You escape!')
            else:
                print('You’re caught.')
        else:
            print("'Instantly defeated you are', says Yoda, whilst coming out of the ship. ")

#---------------------Wizards----------------------------------------
def wizards():
    wc = input("(All questions ar y/n) You are in a wizard duel. Is your wand charged????? ")
    if wc == 'y':
        mana = int(input("What is your mana?(A number from 1 - 100 please) "))
        if mana >= 50:
            spell = input("Is spell lightning (ln) or ice(i)? ")
            if spell == 'ln':
                eshield = input("Is the enemy's shield fire? ")
                if eshield == "y":
                    print('⚡ Lightning pierces the shield — you win!')
                else:
                    print("Enemy absorbs and reflects the spell — you lose HP.")
            else:
                temp = float(input("What is the temperature?(A number from -50 - 50 please)"))
                if temp < 0:
                    print("Spell doubles in power — enemy frozen!")
                else:
                    print("Spell melts mid-air — wasted mana.")
        else:
            potion = input("Is potion available? ")
            if potion == 'y':
                ptype = input("What is the potion type?(Mana, fire, ice, rock) ")
                if ptype == 'mana':
                    print(" You restore mana and continue the duel.") 
                else:
                    print(" Potion backfires — you lose focus.")       
            else:
                print("Enemy takes advantage - critical hit on you! ")
    else:
        staffb = input("Is your staff broken? ")
        if staffb == "y":
            bw = input('Do you have a backup wand? ')
            if bw == 'y':
                print("You use your backup wand, but it has half power.")
            else:
                print("You surrender — no weapon left.")
        else:
            print("You channel energy by hand — risky but powerful.")

#main program

name = input("I am A BOT. What is your name? ")
print(f"Hello {name}")

print("What would you like to do today?")
print("1. Calculator")
print("2. Quiz game")
print("3. Jokes")
print("4. BMI Calculator")
print("5. Rock Paper Scissor")
print("6. Guess the number")
print("7. Flags")
print("8. Brick Breaker/Pong game")
print("9. Dodge the ball")
print("10. Turtle Pattern")
print("11. The Hot and Cold game. ")
print("12. The Spaceship, 'In a galaxy far far away...'")
print('13. The Wizard Duel')


choice = int(input("Choose between 1-13: "))


if choice == 1:
    calc()
elif choice == 2:
    quiz()
elif choice == 3:
    jokes()
elif choice == 4:
    BMICalc()
elif choice == 5:
    rps()
elif choice == 6:
    guessnum()
elif choice == 7:
    flags()
elif choice == 8:
    ponggame()
elif choice == 9:
    dodgeball()
elif choice == 10:
    Turtlepattern()
elif choice == 11:
    hotandcold()
elif choice == 12:
    alien_stuff()
elif choice == 13:
    wizards()
else:
    print("Invalid input. Run again. ") 