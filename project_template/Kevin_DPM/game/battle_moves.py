import arcade
from arcade.csscolor import STEEL_BLUE
import constants

class Battle_Moves:

    def __init__(self):
        self.current_move = 0
        self.moves = ["attempt", "None", "None", "None"]
        self.move_box_height = constants.TEXT_BOX_HEIGHT/2
        self.move_box_width = constants.SCREEN_WIDTH/2
        self.can_show_battle_moves = False
        self.has_chosen_move = False


    def draw_all_moves(self, left, bottom):
        for i in range(len(self.moves)):
            mod_x = -1
            if i%2 == 0:
                mod_x = 1

            mod_y = 1
            if i > 1:
                mod_y = -1

            x = left + (constants.SCREEN_WIDTH/2) - ((self.move_box_width/2) * mod_x)
            y = bottom + ((constants.TEXT_BOX_HEIGHT/2) + ((self.move_box_height/2) * mod_y))
            
            self.draw_move(i, x, y)
            
    def draw_move(self, text_index, x, y):
        color = None
        if self.current_move != text_index:
            color = arcade.csscolor.WHITE
        else:
            color = arcade.csscolor.LIGHT_STEEL_BLUE
        text = self.moves[text_index]
        arcade.draw_rectangle_filled(x, y, constants.SCREEN_WIDTH/2, constants.TEXT_BOX_HEIGHT/2, color)

        arcade.draw_text(text, x - self.move_box_width/2, y - 20, arcade.csscolor.BLACK, 48)