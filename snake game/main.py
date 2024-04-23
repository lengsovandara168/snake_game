import pygame
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import button

# Initialize Pygame
pygame.init()

# Create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

# Load button images
start_img = pygame.image.load('start_btn.png').convert_alpha()
exit_img = pygame.image.load('exit_btn.png').convert_alpha()

# Create button instances
start_button = button.Button(100, 200, start_img, 0.8)
exit_button = button.Button(470, 200, exit_img, 0.8)

# Initialize Pygame font for title

pygame.font.init()
font_title = pygame.font.SysFont('Rebellion Squad', 50)



# Game function
def game_play():
    # screen
    screen = Screen()
    screen.setup(width=900, height=900)
    screen.bgcolor("green")
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    # wall
    def draw_wall():
        wall = Turtle()
        wall.width(20)
        wall.penup()
        wall.speed(0)
        wall.goto(-280, 280)
        wall.pendown()

        for _ in range(4):
            wall.fd(580)  # Increase length to cover the whole screen
            wall.right(90)

    draw_wall()

    # controller
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

        # Detect collision with food.
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall.
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            scoreboard.game_over()

        # Detect collision with tail.
        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

    # Ask user to play again or not?
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

# Game loop
run = True
while run:
    screen.fill((202, 228, 241))
    
    # Draw title
    title_text = font_title.render('Snake Game', True, (255, 255, 255), 'black')
    
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 100))
    screen.blit(title_text, title_rect)

    # Draw buttons
    if start_button.draw(screen):
        game_play()
    if exit_button.draw(screen):
        run = False

    # Event handler
    for event in pygame.event.get():
        # Quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
