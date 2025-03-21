from turtle import Turtle,Screen 

luni = Turtle()

screen = Screen()

luni.shape("turtle") 
luni.shapesize(2,2,1) 
luni.color("#006633") 

luni.speed(10) 

luni.pencolor("#00FF99") 
luni.pensize (7) 

def go_forward():
    luni.forward(10)

def turn_right():
    luni.right(30)

def turn_left():
    luni.left(30) 

screen.listen()

screen.onkeypress(go_forward,"Up")

screen.onkeypress(turn_right,"Right")

screen.onkeypress(turn_left,"Left")


screen.mainloop()