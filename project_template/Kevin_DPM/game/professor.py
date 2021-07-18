import arcade
import constants
import random as r

class Professor(arcade.Sprite):
    

    def __init__(self, images, name, start_x, start_y, attacks, task_size, move_to_give, tip, required_level):
        super().__init__(images[0], constants.CHARACTER_SCALING)
        self.start_x = start_x
        self.start_y = start_y
        self.center_x = start_x
        self.center_y = start_y
        self.professor_name = name
        self.required_level = required_level

        self.steps_max = 5
        self.steps = self.steps_max
        self.step_size = 10
        self.direction_x = 0
        self.direction_y = 0
        self.move_wait_time_max = 50
        self.move_wait_time = self.move_wait_time_max
        self.can_pick_direction = True
        self.border_size = constants.SPRITE_PIXEL_SIZE/1

        self.battle_img = images[1]
        self.task_health_max = task_size
        self.task_health = self.task_health_max

        self.tip = tip

        
        self.battleSprite = arcade.Sprite(self.battle_img, .4)
        self.battleSprite.center_x = constants.SCREEN_WIDTH - 200
        self.battleSprite.center_y = constants.SCREEN_HEIGHT - 200
        self.battleSprite.screen_pos_x = constants.SCREEN_WIDTH - 200
        self.battleSprite.screen_pos_y = constants.SCREEN_HEIGHT - 200

        self.new_move = move_to_give

        self.attack_names = attacks["names"]

        self.attacks_damage = attacks["damage"]
        self.chosen_move = ""

        self.current_text = 0
        self.text_options = []
        self.can_move = False
        #     f"Professor {self.professor_name} wants to battle you! Press 'ENTER' to battle"

            # ]

    def pick_random_attack(self):
        return r.randint(0, len(self.attack_names)-1)

    def set_move(self, index):
        self.chosen_move = self.attack_names[index]

    def pick_random_direction(self):
        choice = [-1]
        random_pick = r.randint(0,3)
        if random_pick < 2 :
            self.direction_x = r.choice(choice)
            self.direction_y = 0

            # Make sure that the professor stays near his start position
            if self.outside_of_x_bounds_left():
                self.direction_x = 1
            elif self.direction_x == 1 and self.outside_of_x_bounds_right():
                self.direction_x = -1

        elif random_pick >= 2:
            self.direction_y = r.choice(choice)
            self.direction_x = 0
            
            # Make sure that the professor stays near his start position
            if self.direction_y == -1 and self.outside_of_y_bounds_down():
                self.direction_y = 0
            elif self.direction_y == 1 and self.outside_of_y_bounds_up():
                self.direction_y = 0
        
        else:
            self.direction_x = 0
            self.direction_y = 0

    def pick_random_wait_time(self):

        self.move_wait_time = r.randint(10, self.move_wait_time_max)

    def outside_of_x_bounds_left(self):
        print(f"Left:{self.center_x} <= {-(self.border_size) + self.start_x}")
        return self.center_x <= -(self.border_size) + self.start_x

    def outside_of_x_bounds_right(self):
        print(f"Right:{self.center_x} >= {(self.border_size) + self.start_x}")
        return self.center_x >= (self.border_size) + self.start_x

    def outside_of_y_bounds_up(self):
        print(f"Up:{self.center_y} >= {(self.border_size) + self.start_y}")
        return self.center_y >= (self.border_size) + self.start_y

    def outside_of_y_bounds_down(self):
        print(f"Down:{self.center_y} <= {(self.border_size) + self.start_y}")
        return self.center_y <= -(self.border_size) + self.start_y


    def move_random(self):
        if self.can_pick_direction:
            if self.move_wait_time <= 0:
                self.pick_random_direction()
                self.can_pick_direction = False
                self.pick_random_wait_time()
            
            else:
                self.move_wait_time -= 1
        else:
            if self.steps <= 0:
                self.can_pick_direction = True
                self.steps = self.steps_max

            else:
                self.change_x = self.direction_x * ((constants.SPRITE_PIXEL_SIZE/4)/self.steps_max)
                self.change_y = self.direction_y * ((constants.SPRITE_PIXEL_SIZE/4)/self.steps_max)
                self.steps -= 1
        

    def follow_path(self, point):
        if self.center_x != point["x"]:
            self.steps = point["x"]/self.step_size
            self.change_x = self.step_size

        elif self.center_y != point["y"]:
            self.change_x = 0
            self.steps = point["y"]/self.step_size
            self.change_y = self.step_size
        
        else:
            self.change_x = 0
            self.change_y = 0
            self.task_health_max = 30
            self.task_health = self.task_health_max
            self.required_level = 5
            self.attack_names = ["Find a job", "Manage a team"]
            self.attacks_damage = [5,6]
            self.can_move = False

            
            


    def move(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
            
    def draw_boundry(self):
        arcade.draw_xywh_rectangle_outline(-self.border_size + self.start_x , -self.border_size + self.start_y, self.border_size*2, self.border_size*2, arcade.csscolor.BLACK, 5)
