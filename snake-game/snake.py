from turtle import Turtle
from time import sleep

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
INIT_POSITION = [(0, 0), (0, -20), (0, -40)]


class Snake:
    def __init__(self):
        self.move_step = 20
        self.all_snakes = []
        self.create_snake()
        self.head = self.all_snakes[0]

    def reset(self, score):
        score.total_score = 0
        for snake in self.all_snakes:
            snake.hideturtle()
            del snake
        sleep(2)
        self.__init__()

    def add_one_snake(self, position):
        """
        Increases the body of the snake.
        """
        # snake -> turtle object
        snake = Turtle('square')
        snake.color('white')
        snake.penup()
        snake.speed('fastest')
        self.all_snakes.append(snake)
        snake.goto(position)

    def extend(self):
        self.add_one_snake(self.all_snakes[-1].position())

    def create_snake(self):
        """
        Initialize the snake.
        """
        for p in INIT_POSITION:
            self.add_one_snake(p)

    def move(self):
        """
        Moves the snake.
        """
        snakes_amount = len(self.all_snakes) * - 1
        for snake_index in range(-1, snakes_amount, -1):
            next_index = snake_index - 1  # in front

            # takes the new position that of the snake (the body part in front of it -> next_index)
            next_x = self.all_snakes[next_index].xcor()
            next_y = self.all_snakes[next_index].ycor()

            self.all_snakes[snake_index].goto((next_x, next_y))

        self.head.forward(self.move_step)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
