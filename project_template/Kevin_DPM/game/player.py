import arcade
import constants

class Player(arcade.Sprite):
    

    def __init__(self, images, start_x, start_y):
        super().__init__(images[0], constants.CHARACTER_SCALING)
        self.center_x = start_x
        self.center_y = start_y
        self.battle_img = images[1]
        self.stamina_max = 8
        self.stamina = 7
        self.battleSprite = arcade.Sprite(self.battle_img, .275)
        self.battleSprite.center_x = start_x
        self.battleSprite.center_y = start_y + constants.TEXT_BOX_HEIGHT
        self.battleSprite.screen_pos_x = start_x
        self.battleSprite.screen_pos_y = start_y + constants.TEXT_BOX_HEIGHT
        self.can_continue_battle = True
        self.monsters = 0
        self.money = 50
        self.level = 1
    
    def draw_level_and_money(self, left, bottom):
        arcade.draw_xywh_rectangle_filled(left, constants.SCREEN_HEIGHT + bottom - 50, constants.SPRITE_PIXEL_SIZE, 50, arcade.csscolor.WHITE)
        arcade.draw_text(f"Level: {self.level}",left, constants.SCREEN_HEIGHT + bottom - 50, arcade.csscolor.BLACK, 30)
        
        arcade.draw_xywh_rectangle_filled(left + constants.SCREEN_WIDTH - constants.SPRITE_PIXEL_SIZE, constants.SCREEN_HEIGHT + bottom - 50, constants.SPRITE_PIXEL_SIZE, 50, arcade.csscolor.WHITE)
        arcade.draw_text(f"${self.money}",left + constants.SCREEN_WIDTH - constants.SPRITE_PIXEL_SIZE, constants.SCREEN_HEIGHT + bottom - 50, arcade.csscolor.BLACK, 30)
