import turtle
import time

# define screen
wn = turtle.Screen()
wn.title = "Pong"
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Score
score_a = 0
score_b = 0

# Movement functions
def paddle_a_up():
    y = paddle_a.ycor() # return y coordinates
    y += 20
    if y>=260: y=260
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() # return y coordinates
    y -= 20
    if y<=-240: y=-240
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() # return y coordinates
    y += 20
    if y>=260: y=260
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() # return y coordinates
    y -= 20
    if y<=-240: y=-240
    paddle_b.sety(y)

def score():
    global score_a, score_b
    if ball.xcor() > 390 : score_a +=1
    elif ball.xcor() < 390 : score_b +=1
    
    pen.clear()
    pen.write("Player A: %s  Player B: %s" % (score_a, score_b), 
    align="center", font=("Courier", 24, "normal"))

    paddle_a.goto(-350, 0)
    paddle_b.goto(350, 0)



# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
    time.sleep(0.00001)
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    # if ball hit upper border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    #i f ball hit lower border
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # if ball reaches right border, means player a score!
    if ball.xcor() > 390:
        score()
        ball.goto(0,0)
        ball.dx *= -1
        

    # if ball reaches left border, means player b score!
    if ball.xcor() < -390:
        score()
        ball.goto(0,0)
        ball.dx *= -1
        

    # Paddle and ball collisions
    # if ball hit the paddle b
    if (ball.xcor() > 340 and ball.xcor() < 350 and
        (ball.ycor() < paddle_b.ycor() + 60) and 
        (ball.ycor() > paddle_b.ycor() - 60)):
        ball.setx(340)
        # change ball's horizontal direction
        ball.dx *= -1

        # if ball hit the paddle's corner and comes from opposite direction
        if  ((ball.dy < 0 and (ball.ycor() > paddle_b.ycor() + 40)) or 
            ((ball.dy > 0 and ball.ycor() < paddle_b.ycor() - 40))):
            # change ball's vertical direction
            ball.dy *=-1

    # if ball hit the paddle a
    if (ball.xcor() < -340 and ball.xcor() > -350 and
        (ball.ycor() < paddle_a.ycor() + 60) and 
        (ball.ycor() > paddle_a.ycor() - 60)):
        ball.setx(-340)
        # change ball's horizontal direction
        ball.dx *= -1

        if  ((ball.dy < 0 and (ball.ycor() > paddle_a.ycor() + 40)) or 
            ((ball.dy > 0 and ball.ycor() < paddle_a.ycor() - 40))):
            # change ball's vertical direction
            ball.dy *=-1
         
    