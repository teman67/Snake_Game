import time
from turtle import Screen, Turtle
from snake import Snake

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")


screen.update()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep((0.1))
    snake.move(20)




screen.exitonclick()