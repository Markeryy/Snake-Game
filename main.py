from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# function to set screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


# create a snake object
snake = Snake()

# create a food object
food = Food()

# create a scoreboard object
scoreboard = Scoreboard()

# start listening for keystrokes
screen.listen()
screen.onkey(key="Up", fun=snake.move_snake_up)
screen.onkey(key="Down", fun=snake.move_snake_down)
screen.onkey(key="Left", fun=snake.move_snake_left)
screen.onkey(key="Right", fun=snake.move_snake_right)


# while game is not over
game_over = False
while (not game_over):
    screen.update()     # update the screen
    time.sleep(0.1)     # wait for 0.1 ms
    snake.move_snake()  # move the snake

    # detect collision with wall
    if (snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or snake.head.ycor() >= 300 or snake.head.ycor() <= -300):
        game_over = True
        scoreboard.game_over()

    # detect collision with snake body
    for body in snake.snake_body[1:]:   # skip the snake head 
        if (snake.head.distance(body) < 10):
            game_over = True
            scoreboard.game_over()

    # detect collision with food
    if (snake.head.distance(food) < 15):    # if the distance of head to food is less than 15 pixels
        food.move_location()
        snake.extend_snake()
        scoreboard.increase_score()


screen.exitonclick()





