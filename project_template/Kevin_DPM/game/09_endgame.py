"""
Platformer Game
"""
import arcade
import time
import random
from text import Text
import constants
from controls import Controls
from scene import Scene
from professor import Professor
from player import Player
from battle_moves import Battle_Moves
from vending_machine import Vending_machine_screen
from mini_map import Mini_map
from kira import Kira
from mini_game import Mini_game

# https://www.youtube.com/watch?v=L_UZvW557lM&ab_channel=TURPAK%7CBackgroundMusicforVideos


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.wall_list = None
        self.temple_list = None
        self.machines_list = None
        self.foreground_list = None
        self.background_list = None
        self.dont_touch_list = None
        self.player_list = None

        self.all_sprites_list = None

        # Separate variable that holds the player sprite
        self.player_sprite = []

        # Our physics engine
        self.physics_engine = None

        # Bring in the controls class
        self._controls = Controls()
        # Bring in the scene class
        self._scene = Scene()
        # Bring in the text class
        self._text = Text()
        # Bring in the Battle_Moves class
        self._battle_moves = Battle_Moves()
        # Bring in the Vending_machine_screen class
        self._vending_machine_screen = Vending_machine_screen()
        # Bring in the Mini_map class
        self._mini_map = Mini_map()
        # Bring in the Kira class
        self._kira = Kira()
        # Bring in the Mini_game class
        self._mini_game = Mini_game()

        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0

        # Keep track of the score
        self.score = 0

        # Where is the right edge of the map?
        self.end_of_map = 0

        # Level
        self.level = 1

        # Load sounds
        # self.music_string = constants.MUSIC_PATH
        self.background_music = [constants.DUB_HUB, constants.HAPPY8_BIT, constants.POWERUP]
        self.battle_music = [constants.DIGESTIVE_BISCUIT, constants.MEGALOVANIA, constants.MOUNTAIN_TRAILS]
        # self.game_over = arcade.load_sound(":resources:sounds/gameover1.wav")
        self.music = None
        self.current_player = None

        # Keep track of whether or not you are in contact with a professor to show text
        self.show_text = False

        self.display_text = ""
        self.display_text_count = 0

        self.with_professor = None

        
    def play_song(self, song):
        """ Play the song. """
        # Stop what is currently playing.
        if self.music:
            self.music.stop(self.current_player)

        # Play the next song
        # print(f"Playing {self.music_list[self.current_song_index]}")
        self.music = arcade.Sound(song, streaming=True)
        self.current_player = self.music.play(constants.MUSIC_VOLUME)
        # This is a quick delay. If we don't do this, our elapsed time is 0.0
        # and on_update will think the music is over and advance us to the next
        # song before starting this one.
        # time.sleep(0.03)

    def setup(self, level):
        """ Set up the game here. Call this function to restart the game. """

        # self.main_menu_img = arcade.load_texture("project_template/Kevin_DPM/assets/images/screens/main_screen.png")
        self.main_menu_img = arcade.load_texture(constants.MAIN_MENU)

        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0

        # Keep track of the score
        self.score = 0

        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.professor_list = arcade.SpriteList()
        self.foreground_list = arcade.SpriteList()
        self.background_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.temple_list = arcade.SpriteList()
        self.kira_list = arcade.SpriteList()

        # Set up the player, specifically placing it at these coordinates.
        main_image_source = constants.KEVIN_STANDING
        battle_image_source = constants.KEVIN_BATTLE
        
        player_images = [main_image_source, battle_image_source]
        self.player_sprite = Player(player_images,
                                            constants.PLAYER_START_X, constants.PLAYER_START_Y)
        self.player_list.append(self.player_sprite)


        # Set up Kira TA
        self.kira_list.append(self._kira)

        # Set up the player, specifically placing it at these coordinates.
        prof_name = "Phillips"
        main_image_source = constants.PHILLIPS_STANDING
        battle_image_source = constants.PHILLIPS_BATTLE
        attacks = {
            "names": ["Program a loop", "Define a function"],
            "damage": [1, 2]
        }
        tip = "Press 'M' to see the map"
        professor_images = [main_image_source, battle_image_source]
        self.professor_sprite = Professor(professor_images, prof_name, 
                                            constants.PHILLIPS_START_X, constants.PHILLIPS_START_Y, attacks, 3, "Monster Drink", tip)
        self.professor_list.append(self.professor_sprite)


        # --- Load in a map from the tiled editor ---

        # Name of the layer in the file that has our platforms/walls
        platforms_layer_name = 'Platforms'
        # Name of the layer that has items for foreground
        foreground_layer_name = 'Foreground'
        # Name of the layer that has items for background
        background_layer_name = 'Background'

        temple_layer_name = 'Temple'

        machines_layer_name = 'Machines'

        # Map name
        map_name = constants.MAP

        # Load Battle image
        self.battle_images = []
        self.battle_images.append(arcade.load_texture(constants.BATTLE_BACKGROUNDS))

        # Read in the tiled map
        my_map = arcade.tilemap.read_tmx(map_name)

        # Calculate the right edge of the my_map in pixels
        self.end_of_map = my_map.map_size.width * constants.GRID_PIXEL_SIZE

        # -- Background
        self.background_list = arcade.tilemap.process_layer(my_map,
                                                            background_layer_name,
                                                            constants.TILE_SCALING)

        # -- Foreground
        self.foreground_list = arcade.tilemap.process_layer(my_map,
                                                            foreground_layer_name,
                                                            constants.TILE_SCALING)

        # -- Platforms
        self.wall_list = arcade.tilemap.process_layer(map_object=my_map,
                                                      layer_name=platforms_layer_name,
                                                      scaling=constants.TILE_SCALING,
                                                      use_spatial_hash=True)
        # -- Temple                                            
        self.temple_list = arcade.tilemap.process_layer(map_object=my_map,
                                                      layer_name=temple_layer_name,
                                                      scaling=constants.TILE_SCALING,
                                                      use_spatial_hash=True)

        self.machines_list = arcade.tilemap.process_layer(map_object=my_map,
                                                      layer_name=machines_layer_name,
                                                      scaling=constants.TILE_SCALING,
                                                      use_spatial_hash=True)

        # --- Other stuff
        # Set the background color
        if my_map.background_color:
            arcade.set_background_color(my_map.background_color)

        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.wall_list)
        # Create the 'physics engine'
        self.physics_engine_prof = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.professor_list)

    
    def _load_all_sprites(self):
        self.all_sprites_list = []
        self.all_sprites_list.append(self.background_list)
        self.all_sprites_list.append(self.wall_list)
        self.all_sprites_list.append(self.professor_list)
        self.all_sprites_list.append(self.kira_list)
        self.all_sprites_list.append(self.player_list)
        self.all_sprites_list.append(self.temple_list)
        self.all_sprites_list.append(self.machines_list)
        self.all_sprites_list.append(self.foreground_list)


    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        self._load_all_sprites()
        arcade.start_render()
        
        # Which scene do we show
        if self._scene.show_main_menu:
            self._scene.main_menu(self.main_menu_img, self.view_left, self.view_bottom)

        elif not self._scene.battle_scene:
            # Draw our sprites
            self._scene.display(self.all_sprites_list)
            if self._vending_machine_screen.show_vending_screen:
                self._vending_machine_screen.draw_vending_screen( self.view_left, self.view_bottom)
            
            if self._controls.can_show_mini_map:
                self._mini_map.draw_map(self.view_left, self.view_bottom)

            if self._kira.showing_game:
                self._mini_game.draw_game(self.view_left, self.view_bottom)


        else:
            if self.with_professor != None:
                self._scene.battle_display(self.player_list[0], self.with_professor, self.view_left, self.view_bottom, self.battle_images[0])
            else: 
                self._scene.battle_scene = False
        print(self._battle_moves.has_chosen_move)
        # Do we show text?
        if self.show_text:
            # Draw our text on the screen, scrolling it with the viewport

            if not self._battle_moves.can_show_battle_moves:
                
                arcade.draw_rectangle_filled(self.view_left + constants.SCREEN_WIDTH/2, self.view_bottom + constants.TEXT_BOX_HEIGHT/2,
                            constants.SCREEN_WIDTH, constants.TEXT_BOX_HEIGHT, arcade.csscolor.WHITE)
                
                
                text = ""
                if not self._scene.battle_scene and not self._kira.with_player:
                    text = self._text.meet_prof_text(self.with_professor.professor_name)
                elif self._kira.with_player:
                    
                    # text_with_check = ""
                    if self._mini_game.won:
                        text_with_check = self._text.print_text(self._kira.text_options[self._kira.current_text][0], show_has_finished=True)
                    elif self._mini_game.lost:
                        text_with_check = self._text.print_text(self._kira.text_options[self._kira.current_text][1], show_has_finished=True)
                    else:
                        text_with_check = self._text.print_text(self._kira.text_options[self._kira.current_text][0], show_has_finished=True)
                    text = text_with_check[0]
                    # print(text_with_check)
                    if not self._kira.showing_game and self._controls.can_proceed and text_with_check[1]:
                        self._text.clear_text()
                        self._kira.current_text += 1

                        if self._kira.current_text != -1:
                            self._kira.showing_game = True

                        self._mini_game.won = False
                        self._mini_game.lost = False
                        self._mini_game.time_left = self._mini_game.time_max
                        

                else:
                    # Check if the player has chosen a move and if the player can still continue
                    if self._battle_moves.has_chosen_move and self.player_list[0].can_continue_battle and self.with_professor.task_health > 0:
                        prof_name = self.with_professor.professor_name
                        text_with_check = self._text.battle_prof_text(prof_name, self.with_professor.chosen_move, self._battle_moves.moves[self._battle_moves.current_move], show_has_finished = True)
                        
                        text = text_with_check[0]


                        if text_with_check[1] and self._controls.can_proceed and self.player_list[0].stamina >= 1:
                            
                            self._battle_moves.has_chosen_move = False
                            self._battle_moves.can_show_battle_moves = True

                        elif text_with_check[1] and self._controls.can_proceed and self.player_list[0].stamina <= 0:
                            self.player_list[0].can_continue_battle = False
                            self._text.clear_text()
                            # self.professor_list

                    elif self.with_professor.task_health <= 0:
                        additional_text = f"You can use the move {self.with_professor.new_move}. Also {self.with_professor.tip}."
                        text_with_check = self._text.battle_won_text(additional_text, show_has_finished = True)
                        
                        text = text_with_check[0]

                        if text_with_check[1] and self._controls.can_proceed:
                            self.play_song(random.choice(self.background_music))
                            self._scene.battle_scene = False
                            self._battle_moves.can_show_battle_moves = False
                            self._text.clear_text()
                            self._battle_moves.has_chosen_move = False

                            # Give the player a new move that the professor has for them if they don't already have it
                            if not self.with_professor.new_move in self._battle_moves.moves: 
                                self._battle_moves.moves[self._battle_moves.moves.index("None")] = self.with_professor.new_move
                                self.player_list[0].stamina_max += 5
                            
                            # Otherwise give them more money
                            else:
                                self.player_list[0].money += 5

                    # If the battle is over
                    elif not self.player_list[0].can_continue_battle:
                        text_with_check = self._text.battle_lost_text(show_has_finished = True)
                        
                        text = text_with_check[0]

                        if text_with_check[1] and self._controls.can_proceed:
                            # if self._scene.battle_scene:
                            self.play_song(random.choice(self.background_music))
                            self._scene.battle_scene = False
                            self._battle_moves.can_show_battle_moves = False
                            self.with_professor.task_health = self.with_professor.task_health_max
                            self.player_list[0].stamina = 1
                            self.player_list[0].can_continue_battle = True
                            self._battle_moves.has_chosen_move = False
                            self._text.clear_text()
                        
                arcade.draw_text(text, 10 + self.view_left, constants.TEXT_BOX_HEIGHT/2 + self.view_bottom - 80,
                            arcade.csscolor.BLACK, 48)
            
            else:
                self._battle_moves.current_move = self._controls.current_index
                self._battle_moves.draw_all_moves(self.view_left, self.view_bottom, self.player_list[0].monsters)
                    

        else:
            self._text.clear_text()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        
        if self._scene.show_main_menu:
            if key == arcade.key.ENTER:
                # Exit main menu
                self._scene.show_main_menu = False
                # Start game music
                # ---------------------------------------------------
                self.play_song(random.choice(self.background_music))
                # ---------------------------------------------------

        elif not self._scene.battle_scene and not self._vending_machine_screen.show_vending_screen and not self._kira.showing_game:
            self._controls.main_scene_pressed(key, modifiers, self.show_text)
            self.player_sprite.change_x, self.player_sprite.change_y = self._controls.change_x, self._controls.change_y
            
            if self.with_professor:
                self._scene.battle_scene = self._controls.can_proceed

            
            if self._scene.battle_scene and self.with_professor:
                self._text.clear_text()
                self._battle_moves.can_show_battle_moves = True

                # Que the battle music!
                self.play_song(random.choice(self.battle_music))

        elif self._vending_machine_screen.show_vending_screen:
            self._controls.vending_screen_pressed(key, modifiers)
            self._controls.update_current_index()
            self._vending_machine_screen.choice = self._controls.current_index

        elif self._kira.showing_game:
            self.player_sprite.change_x, self.player_sprite.change_y = 0,0
            self._controls.mini_game_pressed(key, modifiers)
            self._mini_game.player.change_x = self._controls.change_x
            self._mini_game.stop = False
            

        else:
            self._controls.battle_scene_pressed(key, modifiers, self.show_text)
            if not self._battle_moves.has_chosen_move:
                self._battle_moves.can_show_battle_moves = True
                self._text.clear_text()
                if key == arcade.key.ENTER:
                    self._battle_moves.current_move = self._controls.current_index
                    self._battle_moves.has_chosen_move = True
                    self._battle_moves.can_show_battle_moves = False
                    random_move = self.with_professor.pick_random_attack()
                    self.with_professor.chosen_move = self.with_professor.attack_names[random_move]
                    self.player_list[0].stamina -= self.with_professor.attacks_damage[random_move]
                    if self._battle_moves.moves[self._battle_moves.current_move] == "attempt":
                        self.with_professor.task_health -= 1
                    if self._battle_moves.moves[self._battle_moves.current_move] == "Monster Drink":
                        if self.player_list[0].monsters >= 1:
                            self.player_list[0].stamina = self.player_list[0].stamina_max
                            self.player_list[0].monsters -= 1

            else:                    
                self._battle_moves.can_show_battle_moves = False
                
                if key == arcade.key.ENTER and self.show_text:
                    self._controls.can_proceed = True
                    

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if not self._scene.battle_scene and not self._vending_machine_screen.show_vending_screen and not self._kira.showing_game:
            self._controls.main_scene_released(key, modifiers, self.show_text)
            self.player_sprite.change_x, self.player_sprite.change_y = self._controls.change_x, self._controls.change_y
        elif self._vending_machine_screen.show_vending_screen:
            self._controls.vending_screen_released(key, modifiers)
        elif self._kira.showing_game:
            self._controls.mini_game_released(key, modifiers)
            self._mini_game.player.change_x = self._controls.change_x
        else:
            self._controls.battle_scene_released(key, modifiers, self.show_text)
            self._controls.update_current_index()
            
        

    def update(self, delta_time):
        """ Movement and game logic """
        if not self._scene.show_main_menu:
            professor_collision = arcade.check_for_collision_with_list(self.player_sprite, self.professor_list)

            if len(professor_collision) > 0:
                self.with_professor = professor_collision[0]
                self.show_text = True

                if self._scene.battle_scene:
                    
                    # Repeat Music!
                    if not self.music.is_playing(self.current_player):
                        
                        self.play_song(random.choice(self.battle_music))

                # if professor_collision[0].task_health <= 0:
                    # if self._scene.battle_scene:
                    #     self.play_song(random.choice(self.background_music))
                    # self._scene.battle_scene = False
                    # self._battle_moves.can_show_battle_moves = False


            else:
                self.with_professor = None

                self.show_text = False

            
            vending_machine = arcade.check_for_collision_with_list(self.player_sprite, self.machines_list)
            
            if len(vending_machine) > 0:
                if not self._vending_machine_screen.has_left:
                    # Set the player speed to 0
                    self.player_list[0].change_x = 0
                    self.player_list[0].change_y = 0
                    

                    self._vending_machine_screen.show_vending_screen = True
                    self._vending_machine_screen.determine_output(self._controls.can_proceed, self.player_list[0].money)
                    
                    # If the player decides to leave make sure they pay first
                    # Then reset the amount of monsters bought to 0
                    if self._vending_machine_screen.has_left:
                        self.player_list[0].money -= self._vending_machine_screen.monster_cost * self._vending_machine_screen.monsters_bought
                        self.player_list[0].monsters = self._vending_machine_screen.monsters_bought
                        self._vending_machine_screen.monsters_bought = 0
                else:
                    self._vending_machine_screen.show_vending_screen = False


            else:
                self._vending_machine_screen.show_vending_screen = False
                self._vending_machine_screen.has_left = False

            self._kira.with_player = arcade.check_for_collision(self.player_sprite, self._kira)
            # print(self._kira.current_text)
            if not self._kira.with_player:
                self._kira.current_text = 0
                self._mini_game.won = False
                self._mini_game.lost = False
                self._mini_game.time_left = self._mini_game.time_max

            elif self._kira.with_player and not self.with_professor:
                self.show_text = True
                if self._kira.showing_game and (not self._mini_game.won or not self._mini_game.lost):
                    self._mini_game.update_game()

                    if self._mini_game.won:
                        self._kira.current_text = -1
                        self.player_list[0].stamina_max += 1
                        self._kira.showing_game = False
                        self._mini_game.enemy_list = []
                        self._text.clear_text()
                    elif self._mini_game.lost:
                        self._kira.current_text = -1
                        self._kira.showing_game = False
                        self._mini_game.enemy_list = []
                        self._text.clear_text()



            if not self._scene.battle_scene:
                
                # Repeat Music!
                if not self.music.is_playing(self.current_player):
                    
                    self.play_song(random.choice(self.background_music))

                # Move the professor
                for i in range(len(self.professor_list)):
                    if self.professor_list[i].task_health <= 0 and self.professor_list[i].professor_name == "Phillips":
                        self.professor_list[i].follow_path({"x":75 * constants.SPRITE_PIXEL_SIZE/2, "y":70 * constants.SPRITE_PIXEL_SIZE/2})
                    # self.professor_list[i].move_random()
                    self.professor_list[i].move()
                # prof = self.professor_list[0]
                # print(prof.outside_of_x_bounds_left(),prof.outside_of_x_bounds_right(),prof.outside_of_y_bounds_up(),prof.outside_of_y_bounds_down())


        # Move the player with the physics engine
        self.physics_engine.update()
        # self.physics_engine_prof.update()

        # Track if we need to change the viewport
        changed_viewport = False

        # --- Manage Scrolling ---

        # Scroll left
        left_boundary = self.view_left + constants.LEFT_VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed_viewport = True

        # Scroll right
        right_boundary = self.view_left + constants.SCREEN_WIDTH - constants.RIGHT_VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed_viewport = True

        # Scroll up
        top_boundary = self.view_bottom + constants.SCREEN_HEIGHT - constants.TOP_VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed_viewport = True

        # Scroll down
        bottom_boundary = self.view_bottom + constants.BOTTOM_VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed_viewport = True

        if changed_viewport:
            # Only scroll to integers. Otherwise we end up with pixels that
            # don't line up on the screen
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)

            # Do the scrolling
            arcade.set_viewport(self.view_left,
                                constants.SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                constants.SCREEN_HEIGHT + self.view_bottom)


def main():
    """ Main method """
    window = MyGame()
    window.setup(window.level)
    arcade.run()


if __name__ == "__main__":
    main()