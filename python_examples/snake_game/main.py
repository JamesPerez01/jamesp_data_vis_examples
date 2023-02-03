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


# Functions binded to Play Again key
def no_action():
    """Used to nullify "Play Again" key"""
    pass


def restart_game():
    """Resets and restarts snake game"""
    snake.reset()
    scoreboard.reset()
    food.refresh()
    snake_game()


# Snake Game - Main #
def snake_game():
    """Core of snake game logic"""
    game_on = True
    while game_on:
        # Play again ky binding nullified. Re-binded at game end
        screen.onkey(no_action, "Return")
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
            scoreboard.game_over()
            game_on = False

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 16:
                scoreboard.game_over()
                game_on = False

        # Moves snake forward after going through all 'if' statements
        snake.move()

    # Play again option displayed. Plat again key re-binded
    scoreboard.play_again()
    screen.onkey(restart_game, "Return")


# Initiate snake game
snake_game()

screen.exitonclick()
