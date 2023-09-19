from turtle import Turtle



class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        

    def move(self):
        cor_x = self.xcor() + self.x_move
        cor_y = self.ycor() + self.y_move
        self.goto(cor_x, cor_y)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def ball_reset(self):
        self.setposition(0, 0)
        self.bounce_paddle()
        self.move_speed = 0.1

      




