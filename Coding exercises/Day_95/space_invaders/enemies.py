# Import needed modules
import turtle

# Define global variables
NUM_ENEMIES_PER_ROW = 8
NUM_ROWS = 3
ENEMY_START_X = -300
ENEMY_START_Y = 250
ENEMY_X_SPACING = 50
ENEMY_Y_SPACING = 40
SPEED = 0.3
DROP_DISTANCE = 40
LEFT_EDGE = -360
RIGHT_EDGE = 360


# Define enemies class
class Enemies():
    def __init__(self):
        self.enemies = []
        self.direction = 1
        self.speed = SPEED
        self.create_enemies()

    def create_enemies(self):
        for row in range(NUM_ROWS):
            for column in range(NUM_ENEMIES_PER_ROW):
                enemy = turtle.Turtle()
                enemy.shape('turtle')
                enemy.color('green')
                enemy.setheading(270)
                enemy.penup()
                enemy.speed(0)

                x = ENEMY_START_X + column * ENEMY_X_SPACING
                y = ENEMY_START_Y - row * ENEMY_Y_SPACING
                enemy.goto(x, y)
                self.enemies.append(enemy)

    def move_enemies(self):
        # Check if any enemy hits a wall
        hit_wall = False
        for enemy in self.enemies:
            if enemy.xcor() > RIGHT_EDGE or enemy.xcor() < LEFT_EDGE:
                hit_wall = True
                break

        # If wall hit: reverse + drop down
        if hit_wall:
            self.direction *= -1
            for enemy in self.enemies:
                enemy.sety(enemy.ycor() - DROP_DISTANCE)

        # Move sideways
        for enemy in self.enemies:
            enemy.setx(enemy.xcor() + self.speed * self.direction)

    def remove_enemy(self, enemy):
        enemy.hideturtle()
        if enemy in self.enemies:
            self.enemies.remove(enemy)

    def all_enemies_dead(self):
        return len(self.enemies) == 0

    def reached_player(self, player_y):
        return self.lowest().ycor() <= player_y

    def lowest(self):
        return min(self.enemies, key=lambda e: e.ycor())

    def increase_speed(self, amount=0.02):
        self.speed += amount