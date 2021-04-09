from data import *
from turtle import Turtle
from math import sqrt

def move_everything() -> None:
    """Moves every segment to the position of one index before it"""
    for i in range(len(snake) - 1, 0, -1): 
        snake[i].goto(snake[i-1].xcor(), snake[i-1].ycor())

def move_right() -> None:
    move_everything()
    snake[0].setx(snake[0].xcor() + 20)

def move_left() -> None:
    move_everything()
    snake[0].setx(snake[0].xcor() - 20)
    
def change_up() -> None:
    move_everything()
    snake[0].sety(snake[0].ycor() + 20)
    
def change_down() -> None:
    move_everything()
    snake[0].sety(snake[0].ycor() - 20)

def add_body_part() -> None:
    """Adds a new segment at the end of the snake"""
    last_x = snake[len(snake) - 1].xcor() - SNAKE_BLOCK_WIDTH if len(snake) > 0 else 0
    t = Turtle("square")
    t.penup()
    t.color("white")
    t.speed("fastest")
    t.setpos(last_x, 0)
    snake.append(t)

def check_game_over() -> bool:
    if snake[0].xcor() < -SCREEN_WIDTH / 2 or snake[0].xcor() > SCREEN_WIDTH / 2 or snake[0].ycor() < -SCREEN_HEIGHT / 2 or snake[0].ycor() > SCREEN_HEIGHT / 2: return True
    for seg in snake[1:]: 
        if int(sqrt(pow(seg.xcor() - snake[0].xcor(), 2) + pow(seg.ycor() - snake[0].ycor(), 2))) < SNAKE_BLOCK_WIDTH: return True
    return False