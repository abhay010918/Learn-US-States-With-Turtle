import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S states")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
Guess_the_states = []

while len(Guess_the_states) < 50:
    answer_state = screen.textinput(title=f"{len(Guess_the_states)}/50 States correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in Guess_the_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("learn_states.csv")
        break

    if answer_state in all_states and answer_state not in Guess_the_states:
        Guess_the_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
