import arcade
import constants
import time
import random as r

class Mini_game:
    

    def __init__(self):
        self.time_max = 30
        self.time_left = self.time_max

        self.enemy_list = []

        self.screen_width = constants.SCREEN_WIDTH/2
        self.screen_height = constants.SCREEN_HEIGHT/2
        self.screen_x = self.screen_width - self.screen_width/2
        self.screen_y = self.screen_height - self.screen_height/2    

        self.player = Player(self.screen_x + self.screen_width/2, self.screen_y)

        self.lost = False
        self.won = True

        self.stop = True
    
    def draw_game(self, left, bottom):
        self.draw_background(left, bottom)
        self.draw_enemies(left, bottom)
        self.player.draw(left, bottom)


    def draw_background(self, left, bottom):
        arcade.draw_xywh_rectangle_filled(left + self.screen_x, self.screen_y + bottom, self.screen_width, self.screen_height, arcade.csscolor.DARK_GREY)
        arcade.draw_xywh_rectangle_outline(left + self.screen_x, self.screen_y + bottom, self.screen_width, self.screen_height, arcade.csscolor.BLACK)
        arcade.draw_text(f"{self.time_left:.1f}", left + self.screen_x + self.screen_width, self.screen_y + self.screen_height + bottom, arcade.csscolor.BLACK, 30)

    def draw_enemies(self, left, bottom):
        for enemy in self.enemy_list:
            enemy.draw(left, bottom)
    
    def has_won(self):
        return self.time_left <= 0

    def check_for_collision(self, player, enemy):
        return (player.x + player.size >= enemy.x) and (player.x <= enemy.x + enemy.size) and (player.y + player.size >= enemy.y) and (player.y <= enemy.y + enemy.size)

    def update_game(self):
        if not self.stop:
            random_choice = r.randint(0,1)
            if random_choice == 0:
                self.add_enemy_randomly()
            else:
                self.add_enemy_over_player()
            self.update_time()
            self.player.move()
            self.player.stop_at_borders(self.screen_x, self.screen_x + self.screen_width)
            for i in range(len(self.enemy_list)-1, -1, -1):
                self.enemy_list[i].move_down()
                if self.check_for_collision(self.player, self.enemy_list[i]):
                    self.lost = True
                if self.enemy_list[i].outside_of_border(self.screen_y):
                    self.enemy_list.pop(i)
            
            self.won = self.has_won()
            if self.won:
                self.stop = True

    def add_enemy_randomly(self):
        if int((self.time_left * 10)) % 10 == 0:
            size = r.randint(10, 55)
            x = r.randint(int(self.screen_x), int(self.screen_x + self.screen_width - size))
            y = self.screen_y + self.screen_height - size
            speed = r.randint(10, int(self.time_max - (self.time_left - 15)))/(size - 9)
            self.enemy_list.append(Enemy(x, y, speed, size))

    def add_enemy_over_player(self):
        if int((self.time_left * 10)) % 10 == 0:
            size = r.randint(10, 55)
            
            x = (self.player.x + self.player.size/2 - size/2)
            y = self.screen_y + self.screen_height - size
            speed = r.randint(10, int(self.time_max - (self.time_left - 15)))/(size - 9)
            self.enemy_list.append(Enemy(x, y, speed, size))

    def update_time(self):
        self.time_left -= 0.1
        time.sleep(.1)


class Enemy:
    
    def __init__(self, start_x, start_y, speed, size):
        self.x = start_x
        self.y = start_y
        self.speed = speed
        self.size = size

    def move_down(self):
        self.y -= self.speed

    def outside_of_border(self, bottom_border):
        return self.y < bottom_border

    def draw(self, left, bottom):
        arcade.draw_xywh_rectangle_filled(self.x + left, self.y + bottom, self.size, self.size, arcade.csscolor.WHITE)
        arcade.draw_xywh_rectangle_outline(self.x + left, self.y + bottom, self.size, self.size, arcade.csscolor.BLACK)

class Player:
    
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.size = 50
        self.change_x = 0

    def move(self):
        self.x += self.change_x * self.size

    def stop_at_borders(self, left_border, right_border):
        if self.x <= left_border:
            self.x = left_border + 1
        elif self.x + self.size >= right_border:
            self.x = right_border - self.size - 1

    def draw(self, left, bottom):
        arcade.draw_xywh_rectangle_filled(self.x + left, self.y + bottom, self.size, self.size, arcade.csscolor.GREEN)
        arcade.draw_xywh_rectangle_outline(self.x + left, self.y + bottom, self.size, self.size, arcade.csscolor.BLACK)