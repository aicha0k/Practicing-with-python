import turtle as t
from turtle import Turtle,Screen
import tkinter
import random
robert = Turtle()
my_screen = Screen()
my_screen.listen()

def move_forward():
    robert.forward(10)

def move_backwards():
    robert.backward(10)

def go_counterclockwise():
    new_heading = robert.heading() + 10
    robert.setheading(new_heading)

def go_clockwise():
    new_heading = robert.heading() - 10
    robert.setheading(new_heading)


def clear():
    robert.clear()
    robert.penup( )
    robert.home()
    

my_screen.onkey(key="w", fun=move_forward)
my_screen.onkey(key="s", fun=move_backwards)
my_screen.onkey(key="a", fun=go_counterclockwise)
my_screen.onkey(key="d", fun=go_clockwise)
my_screen.onkey(key="c", fun=clear)

robert.pensize(1)
robert.speed("fastest")
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rand_color = (r,g,b)
    return rand_color


#directions = [0, 90, 180, 270]
# for num in range(100):
#     robert.color(random_color())
#     robert.circle(100,360,100)
#     current_heading = robert.heading()
#     robert.setheading(current_heading + 5)



my_screen.exitonclick()