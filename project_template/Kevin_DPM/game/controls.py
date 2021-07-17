import arcade
import constants


class Controls:

    def __init__(self):
        self.can_proceed = False
        self.is_in_battle_mode = False
        self.change_x = 0
        self.change_y = 0
        self._move_box = [[0,1],[2,3]]
        self.x_index = 0
        self.y_index = 0
        self.current_index = self._move_box[self.y_index][self.x_index]
        self.can_show_mini_map = False
    

    def main_scene_pressed(self, key, modifiers, showing_text):
        """Called whenever a key is pressed. """
        if key == arcade.key.UP or key == arcade.key.W:
            self.change_y = constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.change_y = -constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.change_x = -constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.change_x = constants.PLAYER_MOVEMENT_SPEED
            
        if key == arcade.key.M:
            self.can_show_mini_map = True
            
        if key == arcade.key.ENTER and showing_text:
            self.can_proceed = True

    def main_scene_released(self, key, modifiers, showing_text):
        if key == arcade.key.UP or key == arcade.key.W:
            self.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.change_x = 0
            
        if key == arcade.key.M:
            self.can_show_mini_map = False

        if key == arcade.key.ENTER:
        # if key == arcade.key.ENTER and showing_text:
            self.can_proceed = False

    
    def battle_scene_pressed(self, key, modifiers, showing_text):
        """Called whenever a key is pressed. """
        if key == arcade.key.UP or key == arcade.key.W:
            self.y_index = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.y_index = 1
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.x_index = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.x_index = 1
        
        if key == arcade.key.ENTER and showing_text:
            self.can_proceed = True

        
            
    def battle_scene_released(self, key, modifiers, showing_text):

        if key == arcade.key.ENTER and showing_text:
            self.can_proceed = False


    
    def vending_screen_pressed(self, key, modifiers):
        """Called whenever a key is pressed. """
        self.change_x = 0
        self.change_y = 0
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.x_index = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.x_index = 1
            
        if key == arcade.key.ENTER:
            self.can_proceed = True

        
            
    def vending_screen_released(self, key, modifiers):

        if key == arcade.key.ENTER:
            self.can_proceed = False

    
    def mini_game_pressed(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.change_x = -1
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.change_x = 1
            
        # if key == arcade.key.ENTER:
        #     self.can_proceed = True

        
            
    def mini_game_released(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.change_x = 0

        if key == arcade.key.ENTER:
            self.can_proceed = False


    def update_current_index(self):
        self.current_index = self._move_box[self.y_index][self.x_index]