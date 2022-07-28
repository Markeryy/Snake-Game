from turtle import Turtle

MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.snake_body = []
        self.setup_snake_body()
        self.head = self.snake_body[0]

    def setup_snake_body(self):
        """Set up the snake body."""

        starting_x = 0
        for _ in range(3):
            new_body = Turtle(shape="square")
            new_body.up()
            new_body.color("white")
            new_body.goto(x=starting_x, y=0)
            starting_x -= 20
            self.snake_body.append(new_body)

    def add_body(self, position):
        """Add snake body to a given position"""
        new_body = Turtle(shape="square")
        new_body.up()
        new_body.color("white")
        new_body.goto(position)
        self.snake_body.append(new_body)

    def extend_snake(self):
        self.add_body(self.snake_body[-1].position())  # add to the position of last body

    def move_snake(self):
        """Move the snake."""

        # move following body
        # (body object aside from the snake head)
        for i in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[i-1].xcor()
            new_y = self.snake_body[i-1].ycor()
            self.snake_body[i].goto(new_x, new_y)
        
        # move snake head
        self.head.forward(MOVE_DISTANCE)

    def move_snake_right(self):
        if (self.head.heading() == 180):
            return
        self.head.setheading(0)

    def move_snake_up(self):
        if (self.head.heading() == 270):
            return
        self.head.setheading(90)

    def move_snake_left(self):
        if (self.head.heading() == 0):
            return
        self.head.setheading(180)

    def move_snake_down(self):
        if (self.head.heading() == 90):
            return
        self.head.setheading(270)

    

    