from turtle import Turtle,Screen
import random as rand

luni = Turtle()

screen = Screen()

screen.setup(1000,700)
screen.bgcolor("white")

luni.shape("turtle") 

luni.pensize(7) 

luni.speed(8)

colours = ["#FF0033", "#FF6633", "#FFFF33", "#00FF66", "#000066", "#6600FF", "#9900CC"] 

rounds = 0

while rounds < 1000:

    for x in colours:
        luni.color(x)
        luni.fillcolor(x)
        luni.pencolor(x)

        degree = rand.randint(1, 2)

        if degree == 1:
            luni.right(90)
            luni.forward(40)

        elif degree == 2:
            luni.left(90)
            luni.forward(40)

        width = screen.window_width() / 2
        height = screen.window_height() / 2
        Mwidth = -(screen.window_width () / 2)
        Mheight = -(screen.window_height() / 2)

        if luni.xcor() > width:
            luni.teleport(0,0)

        elif luni.ycor() > height:
            luni.teleport(0,0)

        elif luni.xcor() < Mwidth:
            luni.teleport(0,0)

        elif luni.ycor() < Mheight:
            luni.teleport(0,0)

    rounds = rounds + 1

screen.mainloop() 
