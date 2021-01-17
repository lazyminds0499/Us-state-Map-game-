from turtle import Turtle, Screen
from tatto import States
import pandas
screen = Screen()
screen.title("U.S STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)   # to load any shape for turtle
turtle = Turtle()
turtle.shape(image)
screen.listen()
# def mouse_click_coor(x, y):
#     print(x, y)
# screen.onscreenclick(mouse_click_coor)

guess_list = []
data = pandas.read_csv("50_states.csv")
states_data = data.state
while len(guess_list) < 50:
    answer = screen.textinput(title=f" {len(guess_list)}/50 States correct", prompt="What's the another guess").title()
    if answer == "Exit":
        missing_list = [state for state in states_data if state not in guess_list]
        missed_data = pandas.DataFrame(missing_list)
        missed_data.to_csv("missed_data.csv")
        break
    for state in states_data:
        if answer == state:
            state_data = data[data.state == answer]
            state_x = int(state_data.x)
            state_y = int(state_data.y)
            choice = States((state_x, state_y), answer)
            guess_list.append(answer)

# states not guessed

