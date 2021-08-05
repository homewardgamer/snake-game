import random
from turtle import Turtle
Segments = []
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for postion in STARTING_POS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(postion)
            self.segments.append(new_segment)
        self.segments[0].color("green")

    def move(self):
        for segnum in range(len(self.segments)-1, 0, -1):
            self.segments[segnum].goto(
                self.segments[segnum-1].xcor(), self.segments[segnum-1].ycor())
        self.segments[0].forward(MOVE_DISTANCE)

    def add_segment(self, postion):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(postion)
        self.segments.append(new_segment)


    def extend(self):
        self.add_segment(self.segments[-1].position())
        





    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
