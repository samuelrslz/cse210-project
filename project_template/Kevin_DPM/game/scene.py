import arcade
import constants

class Scene:

    def __init__(self):
        self.response = ""

        self.battle_scene = False
        self.show_main_menu = True
        self.show_intro_message = False
        self.show_end_message = False
        
    def main_menu(self, main_menu_img, intro_text, left, bottom):
        if not self.show_intro_message:
            arcade.draw_texture_rectangle(constants.SCREEN_WIDTH/2 + left, constants.SCREEN_HEIGHT/2 + bottom, 
                                    constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, main_menu_img)
        else:
            arcade.draw_xywh_rectangle_filled(left, bottom, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, arcade.csscolor.WHITE)
            arcade.draw_xywh_rectangle_outline(left + 15, bottom + 15, constants.SCREEN_WIDTH - 30, constants.SCREEN_HEIGHT - 30, arcade.csscolor.BLACK, 50)
            arcade.draw_text(intro_text, left + constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2 + bottom - 50, arcade.csscolor.BLACK, 45, anchor_x="center", anchor_y="center")
    
    def end_scene(self, end_img, left, bottom):
        arcade.draw_texture_rectangle(constants.SCREEN_WIDTH/2 + left, constants.SCREEN_HEIGHT/2 + bottom, 
                                    constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, end_img)
    
    def display(self, characters):
        for character in characters:
            character.draw()
            

    def battle_display(self, player, professor, left, bottom, battle_img):
        arcade.draw_texture_rectangle(constants.SCREEN_WIDTH/2 + left, constants.SCREEN_HEIGHT/2 + bottom, constants.SCREEN_WIDTH,
                                        constants.SCREEN_HEIGHT, battle_img)

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
        bar_current = (player.stamina/player.stamina_max)*(bar_max)
        arcade.draw_xywh_rectangle_filled(left + 10, constants.SCREEN_HEIGHT - 35 + bottom, bar_max, 25, arcade.csscolor.WHITE)
        arcade.draw_xywh_rectangle_filled(left + 10, constants.SCREEN_HEIGHT - 35 + bottom, bar_current, 25, arcade.csscolor.LIGHT_STEEL_BLUE)
        arcade.draw_xywh_rectangle_outline(left + 10, constants.SCREEN_HEIGHT - 35 + bottom, bar_max, 25, arcade.csscolor.BLACK)
        arcade.draw_text(f"Stamina: {player.stamina} / {player.stamina_max}", left + 10, (constants.SCREEN_HEIGHT - 40) + bottom, arcade.csscolor.BLACK, 24)

        # Professor's
        prof_bar_max = constants.SCREEN_WIDTH/4
        prof_bar_current = (professor.task_health/professor.task_health_max)*(prof_bar_max)
        arcade.draw_xywh_rectangle_filled((professor.battleSprite.center_x - prof_bar_max/2), (constants.SCREEN_HEIGHT/2) + bottom, prof_bar_max, 25, arcade.csscolor.WHITE)
        arcade.draw_xywh_rectangle_filled((professor.battleSprite.center_x - prof_bar_max/2), (constants.SCREEN_HEIGHT/2) + bottom, prof_bar_current, 25, arcade.csscolor.DARK_RED)
        arcade.draw_xywh_rectangle_outline((professor.battleSprite.center_x - prof_bar_max/2), (constants.SCREEN_HEIGHT/2) + bottom, prof_bar_max, 25, arcade.csscolor.BLACK)