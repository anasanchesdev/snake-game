from turtle import Screen
from snake import Snake
from food import Food
from score import Score
from pause import Pause
import time


snake = Snake()
screen = Screen()
food = Food('circle')
score = Score()
pause_game = Pause(snake, score, screen, food)

screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('black')
screen.title('s n a k e')

screen.update()

screen.onkey(pause_game.pause, 'Escape')
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

end = False
while not end:

    score.update_score_txt()
    screen.update()
    time.sleep(0.1)

    score.update_highscore()
    snake.move()

    distance_to_food = snake.head.distance(food)
    if distance_to_food < 15:
        score.total_score += 1
        food.refresh()
        snake.extend()

    head_x_cor = snake.head.xcor()
    head_y_cor = snake.head.ycor()
    if head_x_cor > 290 or head_x_cor < -290 or head_y_cor > 290 or head_y_cor < -290:  # hits screen border
        snake.reset(score)

    for segment in snake.all_snakes[1:]:
        distance_to_head = snake.head.distance(segment)
        if distance_to_head < 10 and pause_game.game_state == 1:
            snake.reset(score)

screen.exitonclick()
