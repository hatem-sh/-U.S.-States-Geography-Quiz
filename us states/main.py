import turtle
import csv
import pandas
game_is_on = True
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data['state'].to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(all_states)}", prompt="what's another state's name").title()

    if answer_state == "Exit":
        missing_state = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        stat = data[data.state == answer_state]
        writer.goto(int(stat.x), int(stat.y))
        writer.write(answer_state)










