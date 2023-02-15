import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "us-states-file/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def print_cor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(print_cor)

states = pandas.read_csv("us-states-file/50_states.csv")


def check_answer(answer):
    if answer in all_states:
        return True
    else:
        return False


def write_state(answer):
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    state_row = states[states.state == answer_state]
    t.goto(int(state_row.x), int(state_row.y))
    t.write(f"{state_row.state.item()}")


all_states = states.state.tolist()
guessed_states = []
score = 0

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50   Guess the State", prompt="What is the state name?").title()
    if answer_state == "Exit":
        # missed_states = []
        # for x in all_states:
        #     if x not in guessed_states:
        #         missed_states.append(x)
        missed_states = [x for x in all_states if x not in guessed_states]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if check_answer(answer_state):
        if answer_state not in guessed_states:
            write_state(answer_state)
            guessed_states.append(answer_state)



# turtle.mainloop()