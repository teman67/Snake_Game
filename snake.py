
from turtle import Turtle

position_list = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in position_list:
            self.add_segment(position)

    def add_segment(self,position):
        new_segmnet = Turtle("square")
        new_segmnet.color("white")
        new_segmnet.penup()
        new_segmnet.goto(position)
        self.segment.append(new_segmnet)

    def extend(self):
        self.add_segment(self.segment[-1].position())


    def move(self,dis_move):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(dis_move)

    def up(self):
        if self.head.heading() != DOWN:
            self.segment[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segment[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segment[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.segment[0].setheading(RIGHT)