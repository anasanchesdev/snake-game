from turtle import Turtle
import re
import time

ALIGNMENT = 'center'
FONT1 = ('Courier', 16, 'normal')
FONT2 = ('Courier', 10, 'normal')
FONT3 = ('Arial Black', 16, 'normal')


def set_highscore():
    """
    :return: The latter highscore.
    """
    with open('highscore.txt') as highscore:
        txt = highscore.read()
        regex = re.search(r'\d+\Z', txt)
        print(txt)
        return int(regex.group())


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.total_score = 0
        self.highscore = set_highscore()
        self.hideturtle()
        self.set()
        self.update_score_txt()

    def update_highscore(self):
        if self.total_score > self.highscore:
            with open('highscore.txt', mode='a') as highscore:
                highscore.write(',' + str(self.total_score))
            self.highscore = set_highscore()

    def update_score_txt(self):
        self.clear()
        self.write(arg=f'Score: {self.total_score}', align=ALIGNMENT, font=FONT1)
        self.goto(-192, 230)
        self.write(arg=f'High Score: {self.highscore}', align=ALIGNMENT, font=FONT1)
        self.set()

    def set(self):
        self.penup()
        self.color('white')
        self.goto(-225, 260)
