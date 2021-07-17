import arcade
import constants
import time

class Vending_machine_screen:

    def __init__(self):
        self.text = "Do you want \nto buy a monster?"

        self.monsters_bought = 0
        self.monster_cost = 5

        self.options = ["Yes +1", "No"]

        self.choice = 0

        self.screen_width = constants.SCREEN_WIDTH/2
        self.screen_height = constants.SCREEN_HEIGHT/2
        self.screen_x = self.screen_width - self.screen_width/2
        self.screen_y = self.screen_height - self.screen_height/2

        self.option_width = constants.SPRITE_PIXEL_SIZE*1.5
        self.option_spacing = 20

        self.option_height = constants.SPRITE_PIXEL_SIZE/2

        self.show_vending_screen = False
        self.has_left = False

        self.player_money = 0

    def draw_vending_screen(self, left, bottom):
        self.draw_background(left, bottom)
        self.draw_vending_choice_screen(left, bottom,)

    def draw_vending_choice_screen(self, left, bottom):
        self.draw_vending_text(left, bottom)
        if self.choice == 0:
            self.draw_buttons(self.options[0], (self.screen_x + self.screen_width/2) - self.option_width - self.option_spacing, left, bottom, arcade.csscolor.STEEL_BLUE)
            self.draw_buttons(self.options[1], (self.screen_x + self.screen_width/2) + self.option_spacing, left, bottom, arcade.csscolor.LIGHT_STEEL_BLUE)
        else:
            self.draw_buttons(self.options[0], (self.screen_x + self.screen_width/2) - self.option_width - self.option_spacing, left, bottom, arcade.csscolor.LIGHT_STEEL_BLUE)
            self.draw_buttons(self.options[1], (self.screen_x + self.screen_width/2) + self.option_spacing, left, bottom, arcade.csscolor.STEEL_BLUE)


    def draw_buttons(self, text, x, left, bottom, color):
        arcade.draw_xywh_rectangle_filled(left + x, self.screen_y + self.option_spacing + bottom, self.option_width, self.option_height, color)
        arcade.draw_xywh_rectangle_outline(left + x, self.screen_y + self.option_spacing + bottom, self.option_width, self.option_height, arcade.csscolor.BLACK)
        arcade.draw_text(text, left + x + self.option_width/2, self.screen_y + self.option_height/2 + bottom, arcade.csscolor.BLACK, 30, anchor_x = "center", anchor_y="center")

    def draw_background(self, left, bottom):
        arcade.draw_xywh_rectangle_filled(left + self.screen_x, self.screen_y + bottom, self.screen_width, self.screen_height, arcade.csscolor.WHITE)
        arcade.draw_xywh_rectangle_outline(left + self.screen_x, self.screen_y + bottom, self.screen_width, self.screen_height, arcade.csscolor.BLACK)

    def draw_vending_text(self, left, bottom):
        arcade.draw_text(self.text, (self.screen_x + self.screen_width/2) + left, ((self.screen_y + self.screen_height - self.screen_height/4) - self.option_spacing) + bottom, arcade.csscolor.BLACK, 35, anchor_x="center", anchor_y="center")
        arcade.draw_text(f"Monsters: \n ${self.monsters_bought*self.monster_cost} (${self.monster_cost} / 1)", (self.screen_x + self.screen_width/4) + left, (self.screen_y + self.screen_height/2) + bottom, arcade.csscolor.BLACK, 30, anchor_x="center", anchor_y="center")
        arcade.draw_text(f"Your Money: \n ${self.player_money}", (self.screen_x + self.screen_width - self.screen_width/4) + left, (self.screen_y + self.screen_height/2) + bottom, arcade.csscolor.BLACK, 30, anchor_x="center", anchor_y="center")

    def update_player_money(self, player_money):
        self.player_money = player_money

    def player_has_sufficient_money(self, player_money):
        return player_money >= (self.monsters_bought + 1) * self.monster_cost


    def determine_output(self, hit_enter, player_money):
        # update the players money as shown in the vending machine
        self.update_player_money(player_money)

        if hit_enter:
            if self.choice == 1:
                self.leave_machine()
            
            elif self.choice == 0:
                if self.player_has_sufficient_money(player_money):
                    self.monsters_bought += 1
                    self.options[1] = "Pay/Leave"

                elif self.options[0] == "Pay/Leave":
                    self.leave_machine()
                else:
                    self.text = "You do not have \nenough money"
                    self.options = ["Pay/Leave","Pay/Leave"]

                time.sleep(0.2)

    def reset_text(self):
        self.text = "Do you want \nto buy a monster?"
        self.options = ["Yes", "No"]

    def leave_machine(self):
        self.has_left = True
        self.reset_text()

# set monsters_bought = 0 outside of this class