from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def game_play():
    
    
    #screen

    screen = Screen()
    screen.setup(width=900, height=900)
    screen.bgcolor("green")
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    
    #wall

    def draw_wall():
            wall = Turtle()
            wall.width(20)
            wall.penup()
            wall.speed(0)
            wall.goto(-280, 280)
            wall.pendown()

            for _ in range(4):
                wall.fd(570)  # Increase length to cover the whole screen
                wall.right(90)

    draw_wall()
    #controller
    screen.listen()
    screen.onkey(snake.up, "Up") or screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "Down") or screen.onkey(snake.down, "s")
    screen.onkey(snake.left, "Left") or screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "Right") or screen.onkey(snake.right, "d")
    
    

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        #Detect collision with food.
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        #Detect collision with wall.
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280: #cor = coordinate
            game_is_on = False
            scoreboard.game_over()

        #Detect collision with tail.
        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                game_is_on = False #exit the while loop
                scoreboard.game_over()
    #ask user to play again or not?
    play_again_text = Turtle()
    play_again_text.penup()
    play_again_text.goto(0, -400)
    play_again_text.color("White")
    play_again_text.write(" លេងម្តងទៀតឬអត់? សូមចុច 'space' ", align="center", font=("Khmer OS Muol Light", 22, "bold"))


    def restart_game():
        screen.clear()
        game_play()

    screen.onkey(restart_game, " ")
    screen.listen()

    screen.exitonclick()    

game_play()