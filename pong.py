import turtle

game_window = turtle.Screen()
game_window.title("Pong by Oleg Tielushko")
game_window.bgcolor("black")
game_window.setup(height=600, width=800)
game_window.tracer(0)

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

    #Game functions

#Move Paddle A -Up
def paddle_A_up():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)

#Move Paddle A -Down

#Move Paddle B -Up

#Move Paddle B -Down

#Keyboard binding
game_window.listen()
game_window.onkeypress(paddle_A_up, "W")

while True:
    game_window.update()
