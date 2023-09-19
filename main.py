from turtle import Screen
import time
import random
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong game')
screen.tracer(0)


paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(paddle_r.up, 'Up')
screen.onkeypress(paddle_r.down, 'Down')
screen.onkeypress(paddle_l.up, 'w')
screen.onkeypress(paddle_l.down, 's')





game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    #Detect collision with wall.
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_wall()
    

    #Detect collision with paddles
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320:
        ball.bounce_paddle()
        
    
    if ball.distance(paddle_l) < 50 and ball.xcor() > -320:
        ball.bounce_paddle()
        

    #Detect if ball goes out.
    if ball.xcor() > 390:
        score.count_score_l()
        ball.ball_reset()

    elif ball.xcor() < -390:
        score.count_score_r()
        ball.ball_reset()
        
        
    






















screen.exitonclick()