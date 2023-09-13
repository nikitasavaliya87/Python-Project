import turtle
import pandas

screen=turtle.Screen()
screen.title("u.S. States Games")
image="Angelia\\Day_25_US_State_game\\us-states-game-start\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()


data=pandas.read_csv("Angelia\\Day_25_US_State_game\\us-states-game-start\\50_states.csv")
all_states=data.state.to_list()
guessed_states=[]

while len(guessed_states)<50:

    answer_state=screen.textinput(title=f"{len(guessed_states)}/50 Guess the State", prompt="What's another state's name?").title()
    print(answer_state) 

    if answer_state == "Exit":
        missing_list=[]
        for state in all_states:
            if state not in guessed_states:
                missing_list.append(state)
        print(missing_list)
        new_data=pandas.DataFrame(missing_list)
        new_data.to_csv("Angelia\\Day_25_US_State_game\\us-states-game-start\\State_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(state_data.state.item())
        #t.write(answer_state)






screen.exitonclick()