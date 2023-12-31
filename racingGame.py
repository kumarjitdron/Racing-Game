from turtle import Turtle, Screen
import random
is_race_on= False
screen=Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Make Your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
colors=["red", "orange","yellow", "green", "medium orchid"]
y_position = [100, 180, 0, -100, -180]
turtle_list= []
for turtle_index in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -240, y = y_position[turtle_index])
    turtle_list.append(new_turtle)
if user_bet:
    is_race_on= True
while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 240:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color== user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_dist= random.randint(0,10)
        turtle.forward(rand_dist)



screen.exitonclick()