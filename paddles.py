from turtle import Turtle

P_WIDTH = 5
P_HEIGHT = 1



class Paddle(Turtle):
    def __init__(self, cord):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.resizemode('user')
        self.shapesize(P_WIDTH, P_HEIGHT)
        self.penup()
        self.setposition(cord)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

