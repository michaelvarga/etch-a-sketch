from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_counterclockwise():
    tim.setheading(tim.heading() + 10)

def move_clockwise():
    tim.setheading(tim.heading() - 10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counterclockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="BackSpace", fun=clear)
screen.exitonclick()

# w = forwards
# s = backwards
# a = counter-clockwise
# d = clockwise
# c = clear and reset position