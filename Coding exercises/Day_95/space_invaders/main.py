# Import needed modules
import turtle
from player import Player
from enemies import Enemies
from score import Score
from bullet import Bullet

# Set up playing area - a black screen with a white border
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Space Invaders")
screen.setup(width=800, height=600)
screen.tracer(0)

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-380, -280)
border_pen.pendown()
border_pen.pensize(3)
for _ in range(4):
    border_pen.forward(760)
    border_pen.left(90)
border_pen.hideturtle()

# Initialize player, enemies, bullets and scoreboard and associated movement functions
player = Player()
enemies = Enemies()
score = Score()
bullet = Bullet()
screen.listen()
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")
screen.onkeypress(lambda: bullet.fire(player.xcor(), player.ycor() + 10), "space")

# Define a turtle to write a win/lose message
message = turtle.Turtle()
message.hideturtle()
message.color("red")
message.penup()


# Checker for collisions helper function
def is_collision(t1, t2):
    return t1.distance(t2) < 20


# Main game loop
game_over = False
while not game_over:
    # Move the enemies and bullets at each point
    enemies.move_enemies()
    bullet.move()

    # For each enemy, if a bullet hits, remove them and add to the score
    for enemy in enemies.enemies[:]:
        if bullet.state == "fire" and is_collision(bullet, enemy):
            bullet.reset_bullet()
            enemies.remove_enemy(enemy)
            score.add_point()
            enemies.increase_speed(0.01)

    # Check for all enemies being dead - win condition
    if enemies.all_enemies_dead():
        message.goto(0, 0)
        message.write("YOU WIN!", align="center", font=("Arial", 36, "bold"))
        game_over = True

    # Check for enemies making it to player - lose condition
    for enemy in enemies.enemies:
        if enemy.ycor() <= player.ycor() + 20:
            message.goto(0, 0)
            message.write("GAME OVER", align="center", font=("Arial", 36, "bold"))
            game_over = True
            break

    screen.update()

screen.exitonclick()
