from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.count_s_r = 0
        self.count_s_l = 0
        self.color('white')
        self.penup()
        self.setposition(0, 260)
        self.hideturtle()
        self.update_scoreboard()        

    def update_scoreboard(self):
        self.write(f"{self.count_s_l} :P2 | P1: {self.count_s_r}", align=ALIGNMENT, font=FONT)
    

    def count_score_r(self):
        self.count_s_r += 1
        self.clear()
        self.update_scoreboard()  

    def count_score_l(self):
        self.count_s_l += 1
        self.clear()
        self.update_scoreboard()  