import arcade
import constants

class Mini_map:

    def __init__(self):
        self.map = arcade.load_texture(constants.MINI_MAP)

    
        self.map_width = 722
        self.map_height = 721
        self.map_x = constants.SCREEN_WIDTH/2
        self.map_y = constants.SCREEN_HEIGHT/2

        
        # self.show_map = False

    def draw_map(self, left, bottom):
        arcade.draw_texture_rectangle(left + self.map_x, bottom +self.map_y, self.map_width, self.map_height, self.map)