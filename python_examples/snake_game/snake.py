from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Includes all snake object related attributes"""

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates the initial snake from starting positions"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Adds segment to snake. Called by create_snake at start and by extend when snake collides with food"""
        snake_seg = Turtle('square')
        snake_seg.color("white")
        snake_seg.penup()
        snake_seg.setpos(position)
        self.segments.append(snake_seg)

    def extend(self):
        """Calls add_segment to add segment to snake. Called when snake collides with food"""
        self.add_segment(self.segments[-1].position())

    # Snake Move #
    def move(self):
        """Starts Snake's perpetual forward movement"""
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        """Resets snake to starting position. Called after play_again"""
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    # Snake Movement Keys #
    def up(self):
        """Sets Snake's heading to North (Up)"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Sets Snake's heading to South (Down)"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Sets Snake's heading to West (Left)"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Sets Snake's heading to East (Right)"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
