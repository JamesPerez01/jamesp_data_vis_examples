from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Calling objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Snake key bindings
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Snake Game Start #
game_is_on = True
while game_is_on:
    screen.update()
    # Controls speed of game
    time.sleep(0.095)

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_point()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

    # Moves snake forward after going through all 'if' statements
    snake.move()

screen.exitonclick()
