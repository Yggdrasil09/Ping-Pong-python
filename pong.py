# A ping pong game built by Karthik
# using turtle module

import turtle
# a basic graphic library

win = turtle.Screen()
win.title("A PING-PONG Game")
win.bgcolor('black')
win.setup(width=800,height=600)
win.tracer(0)

#Left Pad
pad_a= turtle.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("white")
pad_a.shapesize(stretch_wid=5,stretch_len=1)
pad_a.penup()
pad_a.goto(-350,0)

# Right Pad
pad_b= turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("white")
pad_b.shapesize(stretch_wid=5,stretch_len=1)
pad_b.penup()
pad_b.goto(350,0)

# Ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(350,0)


while True:
    win.update()