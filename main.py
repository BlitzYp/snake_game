import turtle
from random import randint
from typing import List
from math import sqrt
from data import *
from controls_snake import *
from time import sleep

def setup_screen(screen: turtle.Screen) -> None:
    """Sets up the screen for input handling"""
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.title("Snake game")
    screen.bgcolor("black")
    screen.onkeypress(move_right, "Right")
    screen.onkeypress(move_left, "Left")
    screen.onkeypress(change_up, "Up")
    screen.onkeypress(change_down, "Down")   
    screen.tracer(8, 25)
    screen.listen()

def change_food_location(food: turtle.Turtle) -> None:
    x,y = randint(-SCREEN_WIDTH / 2, SCREEN_WIDTH / 2), randint(-SCREEN_HEIGHT / 2, SCREEN_HEIGHT / 2)
    food.goto(x,y)

def check_collision(food: turtle.Turtle) -> bool:
    return int(sqrt(pow(food.xcor() - snake[0].xcor(), 2) + pow(food.ycor() - snake[0].ycor(), 2))) < 15

if __name__ == "__main__":
    # Rendering the original snake
    screen = turtle.Screen()
    setup_screen(screen)
    for _ in range(3): 
        add_body_part()

    # Setting up the food turtle
    food = turtle.Turtle("circle")
    food.penup()
    food.color("green")
    change_food_location(food)

    # Setting up the leaderboard
    score = turtle.Turtle()
    score.setpos(0, SCREEN_HEIGHT / 2 - 40)
    score.hideturtle()
    score.penup()
    score.color("red")
    counter = 0
    score.write(f"Score: {counter}", move=True, align="center", font=("Arial", 30, "normal"))

    # The game loop
    while True:
        screen.update()
        if check_collision(food): 
            add_body_part()
            change_food_location(food)
            counter += 1
            score.clear()
            score.setpos(0, SCREEN_HEIGHT / 2 - 40)
            score.write(f"Score: {counter}", move=True, align="center", font=("Arial", 30, "normal"))
        if check_game_over(): 
            score.setpos(0,0)
            score.color("red")
            score.write("GAME OVER", move=True, align="center", font=("Arial", 30, "normal"))
            sleep(2)
            break
