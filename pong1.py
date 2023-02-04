import turtle
## use winsound for windows
import winsound

# import sound
wn = turtle.Screen()

wn.title("Pong By Hasib")

wn.bgcolor("Red")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# pddle 1

padle_a = turtle.Turtle()
padle_a.speed(0)
padle_a.shape("square")
padle_a.color("black")
padle_a.shapesize(stretch_wid=5, stretch_len=1)

padle_a.penup()
padle_a.goto(-350, 0)

# paddle2

padle_b = turtle.Turtle()
padle_b.speed(0)
padle_b.shape("square")
padle_b.color("black")
padle_b.shapesize(stretch_wid=5, stretch_len=1)

padle_b.penup()
padle_b.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = .1
ball.dy = .1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()

pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 16, "bold"))


# function

def paddle_a_up():
    y = padle_a.ycor()
    y += 20
    padle_a.sety(y)


def paddle_a_dwn():
    y = padle_a.ycor()
    y -= 20
    padle_a.sety(y)


def paddle_b_up():
    y = padle_b.ycor()
    y += 20
    padle_b.sety(y)


def paddle_b_dwn():
    y = padle_b.ycor()
    y -= 20
    padle_b.sety(y)


# Keyboard Binding

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_dwn, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_dwn, "Down")

# main game loop

while True:
    wn.update()
    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border chacking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_FILENAME)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_FILENAME)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 16, "bold"))
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 16, "bold"))

    # paadle & ball collisons
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < padle_b.ycor() + 50 and ball.ycor() > padle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_FILENAME)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < padle_a.ycor() + 50 and ball.ycor() > padle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_FILENAME)
