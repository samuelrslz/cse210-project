import arcade
import constants

class Kira(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.KIRA_IMG, constants.CHARACTER_SCALING)
        self.center_x = constants.KIRA_X
        self.center_y = constants.KIRA_Y
        self.with_player = False

        self.current_text = 0
        self.text_options = [["Would you like to increase your stamina? If so press enter!"],
                            ["Avoid the white squares and last for 30 seconds."],
                            ["Congratulations, you won! You increased your stanima by one.", "I'm sorry, but you lost, try again next time."]]

        self.showing_game = False
        
        
    # def