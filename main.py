from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random

# SCREEN SETUP
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Pixel Serpent")
screen.tracer(0)
poison_timer_start = None

serpent = Snake()
food = Food()
if random.randint(0, 5) != 0:
    food.normal_food()
    poison_timer_start = None
else:
    food.poison()
    poison_timer_start = time.time()
_scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(serpent.up, "Up")
screen.onkeypress(serpent.down, "Down")
screen.onkeypress(serpent.left, "Left")
screen.onkeypress(serpent.right, "Right")

game_on = True

while game_on:
    time.sleep(0.07)
    screen.update()
    serpent.move()
    if serpent.serpent_head.distance(food) < 15:
        if food.color()[0] == "yellow":
            print("Dead innit")
            _scoreboard.decrease_score()
        else:
            print("live")
            _scoreboard.increase_score()
            serpent.grow_snake()
        food.reset()
        food.hideturtle()
        food = Food()
        if random.randint(0, 5) != 0:
            food.normal_food()
            poison_timer_start = None
        else:
            food.poison()
            poison_timer_start = time.time()
    # Checking if Poison and not eaten for a certain time period
    if poison_timer_start:
        if time.time() - poison_timer_start >= 5:
            print("Poison expired")
            food.reset()
            food.hideturtle()
            food = Food()
            if random.randint(0, 5) != 0:
                food.normal_food()
                poison_timer_start = None
            else:
                food.poison()
                poison_timer_start = time.time()
    # Checking Collision with borders
    if serpent.serpent_head.xcor() > 280 or serpent.serpent_head.xcor() < -280 or serpent.serpent_head.ycor() > 280 or serpent.serpent_head.ycor() < -280:
        time.sleep(1)
        _scoreboard.reset()
        serpent.reset()

    # Checking Collision with snake itself
    for x in range(1, len(serpent.snake)):
        if serpent.serpent_head.distance(serpent.snake[x]) < 10:
            time.sleep(1)
            _scoreboard.reset()
            serpent.reset()
            break
screen.exitonclick()
# CREDITS: a.shahmir
