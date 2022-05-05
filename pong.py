import turtle

#Window Setup

wn = turtle.Screen()
wn.title("Pong Game by Kailyn Lo :D")
wn.bgcolor("royal blue")
wn.setup(width=800,height=600)
wn.tracer(0)

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("green yellow")
paddle_a.shapesize(stretch_wid = 5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("green yellow")
paddle_b.shapesize(stretch_wid = 5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#net
net = turtle.Turtle()
net.speed(0)
net.shape("square")
net.color("green yellow")
net.shapesize(stretch_wid= 50, stretch_len=0.2)
net.penup()
net.goto(0,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("green yellow")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0,0)
ball.dx = 0.15
ball.dy = 0.15

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("green yellow")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align= "center", font=("Courier New", 24, "normal"))

#score

score_a = 0
score_b = 0

#functions 
def paddle_a_up():
    y = paddle_a.ycor()
    y = y + 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y = y - 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y = y + 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y = y - 20
    paddle_b.sety(y)

#keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


#main game loop

while True:
    wn.update()

    #boarder checking

    #top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = ball.dy * -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = ball.dy * -1
    
    #Right and Left
    if ball.xcor()> 350:
        score_a = score_a + 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align= "center", font= ("Courier New", 24, "normal"))
        ball.goto(0,0)
        ball.dx = ball.dx * -1

    if ball.xcor()< -350:
        score_b = score_b + 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align= "center", font= ("Courier New", 24, "normal"))
        ball.goto(0,0)
        ball.dx = ball.dx * -1

    #move the ball
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    


    # paddle and ball collisions

    if (ball.xcor() < -340 and ball.xcor() > -350) and ball.ycor() < paddle_a.ycor() +50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(-340)
        ball.dx = ball.dx * -1
    elif (ball.xcor() > 340 and ball.xcor() < 350) and ball.ycor() < paddle_b.ycor() +50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(340)
        ball.dx = ball.dx * -1