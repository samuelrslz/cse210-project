import arcade
import constants
import random as r

class Professor(arcade.Sprite):
    

    def __init__(self, images, name, start_x, start_y, attacks):
        super().__init__(images[0], constants.CHARACTER_SCALING)
        self.center_x = start_x
        self.center_y = start_y
        self.professor_name = name
        self.battle_img = images[1]
        self.task_health = 10

        
        self.battleSprite = arcade.Sprite(self.battle_img, .4)
        self.battleSprite.center_x = constants.SCREEN_WIDTH - 200
        self.battleSprite.center_y = constants.SCREEN_HEIGHT - 200

        self.attack_names = attacks["names"]

        self.attacks_damage = attacks["damage"]
        self.chosen_move = ""

        self.current_text = 0
        # self.text_options = [
        #     f"Professor {self.professor_name} wants to battle you! Press 'ENTER' to battle"

            # ]

    def pick_random_attack(self):
        return r.randint(0, len(self.attack_names)-1)

    def set_move(self, index):
        self.chosen_move = self.attack_names[index]