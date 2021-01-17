from turtle import Turtle


class States(Turtle):
    def __init__(self, posi, state_name):
        super(States, self).__init__()
        self.penup()
        self.hideturtle()
        self.goto(posi)
        self.write(arg=f"{state_name}", align="center", font=("courier", 10, "normal"))
