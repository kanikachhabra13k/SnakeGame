from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import  time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on =True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food)<20:
        food.refresh()
        score.increase_score()
        snake.extend()

    if snake.segments[0].xcor()>285 or snake.segments[0].xcor()<-285 or snake.segments[0].ycor()<-285 or snake.segments[0].ycor()>285:
        score.high_score()
        snake.reset()


    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment)<10:
            score.high_score()
            snake.reset()



# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
#     def breathe(self):
#         print("Inhale, exhale.")
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#     def breathe(self):
#         super().breathe()
#         print("doing this underwater.")
#     def swim(self):
#         print("moving in water.")





screen.exitonclick()