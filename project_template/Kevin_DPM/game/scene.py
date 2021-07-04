import arcade
import constants

class Scene:

    def __init__(self):
        self.response = ""

        self.battle_scene = False

    
    def display(self, characters):
        for character in characters:
            character.draw()

    def battle_display(self, player, professor):
        player.battleSprite.draw()
        
        professor.battleSprite.draw()
        self.draw_bars(player, professor)

    def draw_bars(self, player, professor):
        # Player's
        bar_max = constants.SCREEN_WIDTH/2 
        bar_current = (player.stanima/player.stanima_max)*(constants.SCREEN_WIDTH/2)
        arcade.draw_rectangle_filled(player.battleSprite.center_x, constants.SCREEN_HEIGHT - 25, bar_max, 25, arcade.csscolor.WHITE)
        arcade.draw_rectangle_filled(player.battleSprite.center_x, constants.SCREEN_HEIGHT - 25, bar_current, 25, arcade.csscolor.LIGHT_STEEL_BLUE)

        # Professor's
        arcade.draw_text(f"Task: {professor.task_health}", professor.battleSprite.center_x - 48, constants.TEXT_BOX_HEIGHT - 20, arcade.csscolor.WHITE, 48)