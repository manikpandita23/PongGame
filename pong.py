import turtle

sc = turtle.Screen()
sc.title("Pong Game")
sc.bgcolor("white")
sc.setup(width=1000, height=600)

left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=5, stretch_len=1)
left_pad.penup()
left_pad.goto(-400, 0)