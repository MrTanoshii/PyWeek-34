import arcade
import math

class Enemy(arcade.Sprite):

    def __init__(self,
                 image,
                 scale,
                 position_list,
                 hp,
                 speed,
                 armor_type=None,
                 flying=False,
                 boss=False
                 ):

        super().__init__(image, scale)

        self.position_list = position_list
        self.hp_current = hp
        self.hp_max = hp
        self.speed = speed
        self.armor_type = armor_type
        self.flying = flying
        self.boss = boss

        self.cur_position = 0
        self.poisoned = False
        self.slowed = False


    def update(self):

        start_x = self.center_x
        start_y = self.center_y

        dest_x = self.position_list[self.cur_position][0]
        dest_y = self.position_list[self.cur_position][1]

        x_diff = dest_x - start_x
        y_diff = dest_y - start_y

        angle = math.atan2(y_diff, x_diff)

        distance = math.sqrt((self.center_x - dest_x) ** 2 + (self.center_y - dest_y) ** 2)

        speed = min(self.speed, distance)
        if self.slowed and distance > self.speed * .5:
            speed /= 2

        change_x = math.cos(angle) * speed
        change_y = math.sin(angle) * speed

        self.center_x += change_x
        self.center_y += change_y

        distance = math.sqrt((self.center_x - dest_x) ** 2 + (self.center_y - dest_y) ** 2)

        if distance <= self.speed:
            self.cur_position += 1
            if self.cur_position >= len(self.position_list):
                # enemy has reached destination
                # take away hps from player
                ...




'''
import arcade
from enemy.enemy import Enemy
# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_ENEMY = 0.5
ENEMY_SPEED = 3.0

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Follow Path Simple Example"


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Variables that will hold sprite lists
        self.player_list = None
        self.enemy_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/"
                                           "femalePerson_idle.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # List of points the enemy will travel too.
        position_list = [[50, 50],
                         [700, 50],
                         [700, 500],
                         [50, 500]]

        # Create the enemy
        enemy = Enemy(":resources:images/animated_characters/robot/robot_idle.png",
                      SPRITE_SCALING_ENEMY,
                      position_list, 100, 5)

        # Set initial location of the enemy at the first point
        enemy.center_x = position_list[0][0]
        enemy.center_x = position_list[0][1]

        # Add the enemy to the enemy list
        self.enemy_list.append(enemy)

    def on_draw(self):
        """ Draw everything """
        self.clear()
        self.enemy_list.draw()
        self.player_list.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.enemy_list.update()


def main():
    """ Main function """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()


'''