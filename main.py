from turtle import Turtle,Screen
import turtle
import pandas as pd
from scoreboard import ScoreBoard

data = pd.read_csv("states.csv")
states = data.state.to_list()
# states = [_.lower() for _ in states]
# print(states)
t = Turtle()
s = Screen()
s.setup(800,800)
score = ScoreBoard()
t.ht()
t.penup()
s.bgpic("india_states.gif")
game_on = True
while(game_on):
    user_input = turtle.textinput("Enter a state", "Enter exit to quit").title()
    if user_input in states:
        xcor = data.x[data.state == user_input]
        ycor = data.y[data.state == user_input]
        t.goto(int(xcor)-10,int(ycor))
        t.write(user_input)
        score.new_score()
    elif(score.send_score() == 30):
        score.game_won()
        game_on = False
    elif(user_input == 'Exit'):
        score.game_over()
        game_on = False
s.exitonclick()