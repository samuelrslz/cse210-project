import arcade
import constants

class Scene:

    def __init__(self):
        self.response = ""

        self.battle_scene = False

    
    def display(self, characters):
        for character in characters:
            character.draw()

    def battle_display(self, player, professor, left, bottom):
        player.battleSprite.center_x = player.battleSprite.screen_pos_x + left
        player.battleSprite.center_y = player.battleSprite.screen_pos_y + bottom
        player.battleSprite.draw()
        
        professor.battleSprite.center_x = professor.battleSprite.screen_pos_x + left
        professor.battleSprite.center_y = professor.battleSprite.screen_pos_y + bottom
        professor.battleSprite.draw()
        self.draw_bars(player, professor, left, bottom)

    def draw_bars(self, player, professor, left, bottom):
        # Player's
        bar_max = constants.SCREEN_WIDTH/2 
        bar_current = (player.stanima/player.stanima_max)*(constants.SCREEN_WIDTH/2)
        arcade.draw_xywh_rectangle_filled(left + 10, constants.SCREEN_HEIGHT - 35 + bottom, bar_max, 25, arcade.csscolor.WHITE)
        arcade.draw_xywh_rectangle_filled(left + 10, constants.SCREEN_HEIGHT - 35 + bottom, bar_current, 25, arcade.csscolor.LIGHT_STEEL_BLUE)

        # Professor's
        arcade.draw_text(f"Task: {professor.task_health}", (professor.battleSprite.center_x - 48), (constants.TEXT_BOX_HEIGHT - 10) + bottom, arcade.csscolor.WHITE, 48)