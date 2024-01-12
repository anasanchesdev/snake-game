from turtle import Turtle

FONT1 = ('Heather', 60, 'normal')
FONT2 = ('Copperplate Gothic Bold', 40, 'normal')
FONT3 = ('Courier', 12, 'normal')


class Pause(Turtle):
    def __init__(self, snake, score, screen, food):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.game_state = 1  # 1: unpaused | -1: paused
        self.snake = snake
        self.score = score
        self.screen = screen
        self.food = food
        self.pause_msg()

    def pause_msg(self):
        self.goto(-90, -270)
        self.color('white')
        self.write('(press ESC to pause)', font=FONT3)

    def pause(self):
        self.game_state *= -1
        if self.game_state == -1:

            for snake in self.snake.all_snakes:
                snake.hideturtle()

            self.screen.bgcolor('white')
            self.food.hideturtle()
            self.color('black')
            self.goto(-10, -30)
            self.write('II', font=FONT1)
            self.goto(-120, 150)
            self.write('PAUSED', font=FONT2)
            self.goto(-100, -270)
            self.color('gray')
            self.write('(press ESC to unpause)', font=FONT3)
            self.goto(-10, -30)

            self.snake.move_step = 0

        else:

            for snake in self.snake.all_snakes:
                snake.showturtle()

            self.clear()
            self.food.showturtle()
            self.pause_msg()
            self.screen.bgcolor('black')
            self.snake.move_step = 20
