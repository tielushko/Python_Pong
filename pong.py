import turtle
import winsound

game_window = turtle.Screen()
game_window.title("Pong by Oleg Tielushko")
game_window.bgcolor("black")
game_window.setup(height=600, width=800)
game_window.tracer(0)

#Score
score_a = 0
score_b = 0

#Main game loop

    #Paddle A
paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.color("white")
paddle_A.shapesize(stretch_wid=5,stretch_len=1)
paddle_A.penup()
paddle_A.goto(-350,0)

    #Paddle B
paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("white")
paddle_B.shapesize(stretch_wid=5,stretch_len=1)
paddle_B.penup()
paddle_B.goto(350,0)

    #Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.25 #ball speed over x axis - delta x
ball.dy = 0.25

# Pen - for drawing the score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 24, "normal"))

#Game functions

#Move Paddle A -Up
def paddle_A_up():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)

#Move Paddle A -Down
def paddle_A_down():
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)

#Move Paddle B -Up
def paddle_B_up():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y)

#Move Paddle B -Down
def paddle_B_down():
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)

#Keyboard binding
game_window.listen()
game_window.onkeypress(paddle_A_up, "w")
game_window.onkeypress(paddle_A_down, "s")
game_window.onkeypress(paddle_B_up, "Up")
game_window.onkeypress(paddle_B_down, "Down")

while True:
    game_window.update()

    #Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking conditions
    
    #top of the screen
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("jumping.wav", winsound.SND_ASYNC)

    #bottom of the screen
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("jumping.wav", winsound.SND_ASYNC)

    #right of the screen - out of bounds, reset to 0,0 and reverse direction
    if ball.xcor() > 390:
        winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}   Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    #left of the screen - out of bounds, reset to 0,0 and reverse direction
    if ball.xcor() < -390:
        winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}   Player B: {score_b}", align="center", font=("Courier", 24, "normal"))


    #paddle and ball collisions - right paddle
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_B.ycor() + 40 and ball.ycor() > paddle_B.ycor() - 40):
        winsound.PlaySound("jumping.wav", winsound.SND_ASYNC)
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_A.ycor() + 40 and ball.ycor() > paddle_A.ycor() - 40):
        winsound.PlaySound("jumping.wav", winsound.SND_ASYNC)
        ball.setx(-340)
        ball.dx *= -1
