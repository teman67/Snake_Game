import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")


screen.update()

game_is_on = True
score = 0

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move(20)

    # Detect collision with food
    if snake.head.distance(food) < 15:
        print("FOOOD!!")
        snake.extend()
        food.refresh()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segment[1:]:
        # if segment == snake.head:
        #     pass
        # elif snake.head.distance(segment) < 10:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()






screen.exitonclick()