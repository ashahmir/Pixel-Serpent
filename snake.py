from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.x_cord = 0
        self.snake = []
        for x in range(3):
            serpent = Turtle()
            serpent.shape("square")
            if x == 0:
                serpent.color("brown")
            else:
                serpent.color("red")
            serpent.penup()
            serpent.goto(self.x_cord, 0)
            self.snake.append(serpent)
            self.x_cord -= 20
        self.serpent_head = self.snake[0]

    def move(self):
        for x in range(len(self.snake) - 1, 0, -1):
            x_pos = self.snake[x - 1].xcor()
            y_pos = self.snake[x - 1].ycor()
            self.snake[x].goto(x_pos, y_pos)
        self.serpent_head.forward(20)

    def grow_snake(self):
        serpent = Turtle()
        serpent.penup()
        serpent.shape("square")
        serpent.color("red")
        serpent.goto(self.snake[-1].position())
        self.snake.append(serpent)

    def up(self):
        if self.serpent_head.heading() != DOWN:
            self.serpent_head.setheading(90)

    def down(self):
        if self.serpent_head.heading() != UP:
            self.serpent_head.setheading(270)

    def right(self):
        if self.serpent_head.heading() != LEFT:
            self.serpent_head.setheading(0)

    def left(self):
        if self.serpent_head.heading() != RIGHT:
            self.serpent_head.setheading(180)

    def reset(self):
        for parts in self.snake:
            parts.goto(1000,1000)
        self.snake.clear()
        self.x_cord = 0
        for x in range(3):
            serpent = Turtle()
            serpent.shape("square")
            if x == 0:
                serpent.color("brown")
            else:
                serpent.color("red")
            serpent.penup()
            serpent.goto(self.x_cord, 0)
            self.snake.append(serpent)
            self.x_cord -= 20
        self.serpent_head = self.snake[0]

# CREDITS: a.shahmirf
