import  turtle
import  pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()


us_data = pandas.read_csv("50_states.csv")
all_states = us_data['state'].to_list()

guess_state = []
while len(guess_state) < 50:
    answer_state = screen.textinput(f"{len(guess_state)}/50 states correct", "What is another state?").title()

    if  answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if  state not in guess_state:
                missing_state.append(state)
        data_missing = pandas.DataFrame(missing_state)
        data_missing.to_csv("You_missed_these_states.csv")
        break
    if  answer_state  in  all_states:
        guess_state.append(answer_state)
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        location = us_data[us_data.state == answer_state]
        state.goto(int(location.x), int(location.y))
        state.write(answer_state)

turtle.mainloop()
