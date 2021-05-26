from turtle import Turtle, Screen

timmy = Turtle()
timmy.width(2)
screen = Screen()

screen.listen()


def move_forward():
    timmy.forward(20)


def move_backward():
    timmy.backward(20)


def counter_clockwise():
    timmy.setheading(timmy.heading() + 5)


def clockwise():
    timmy.setheading(timmy.heading() - 5)


def clear_drawing():
    timmy.clear()
    timmy.up()
    timmy.home()
    timmy.down()


screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=counter_clockwise, key="a")
screen.onkey(fun=clockwise, key="d")
screen.onkey(fun=clear_drawing, key="c")

screen.exitonclick()
