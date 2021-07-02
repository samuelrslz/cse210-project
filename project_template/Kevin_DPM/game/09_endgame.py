"""
Platformer Game
"""
import arcade
from text import Text
import constants

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
        self.foreground_list = None
        self.background_list = None
        self.dont_touch_list = None
        self.player_list = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        # Our physics engine
        self.physics_engine = None

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
        self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")
        self.game_over = arcade.load_sound(":resources:sounds/gameover1.wav")

        # Keep track of whether or not you are in contact with a professor to show text
        self.show_text = False

        self.display_text = ""
        self.display_text_count = 0

        self.show_battle_scene = False

    def setup(self, level):
        """ Set up the game here. Call this function to restart the game. """

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

        # Set up the player, specifically placing it at these coordinates.
        image_source = "project_template/Kevin_DPM/assets/images/custom_tiles/phillips.png"
        self.player_sprite = arcade.Sprite(image_source, constants.CHARACTER_SCALING)
        self.player_sprite.center_x = constants.PLAYER_START_X
        self.player_sprite.center_y = constants.PLAYER_START_Y
        self.player_list.append(self.player_sprite)



        # Set up the player, specifically placing it at these coordinates.
        image_source = "project_template/Kevin_DPM/assets/images/custom_tiles/phillips.png"
        self.professor_sprite = arcade.Sprite(image_source, constants.CHARACTER_SCALING)
        self.professor_sprite.center_x = constants.PHILLIPS_START_X
        self.professor_sprite.center_y = constants.PHILLIPS_START_Y
        self.professor_list.append(self.professor_sprite)


        # --- Load in a map from the tiled editor ---

        # Name of the layer in the file that has our platforms/walls
        platforms_layer_name = 'Platforms'
        # Name of the layer that has items for foreground
        foreground_layer_name = 'Foreground'
        # Name of the layer that has items for background
        background_layer_name = 'Background'

        # Map name
        map_name = f"project_template/Kevin_DPM/assets/maps/byui.tmx"

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



    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()
        
        if not self.show_battle_scene:
            # Draw our sprites
            self.wall_list.draw()
            self.background_list.draw()
            self.wall_list.draw()
            self.professor_list.draw()
            self.player_list.draw()
            self.foreground_list.draw()

        else:
            self.professor_list.draw()
        

        if self.show_text:
            # Draw our score on the screen, scrolling it with the viewport
            arcade.draw_rectangle_filled(self.view_left + constants.SCREEN_WIDTH/2, self.view_bottom + constants.TEXT_BOX_HEIGHT/2, constants.SCREEN_WIDTH, constants.TEXT_BOX_HEIGHT, arcade.csscolor.WHITE)
            score_text = f"Ready to Battle Professor Phillips? Press enter to continue."
            
            if self.display_text == "":
                self.display_text_count = 0
            if self.display_text.replace("\n", "") != score_text:
                self.display_text += score_text[self.display_text_count]
                if self.display_text_count % 35 == 0 and self.display_text_count > 0:
                    self.display_text += "\n"
                self.display_text_count += 1
            arcade.draw_text(self.display_text, 10 + self.view_left, constants.TEXT_BOX_HEIGHT/2 + self.view_bottom - 80,
                         arcade.csscolor.BLACK, 48)

        else:
            self.display_text = ""

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if not self.show_battle_scene:
            if key == arcade.key.UP or key == arcade.key.W:
                self.player_sprite.change_y = constants.PLAYER_MOVEMENT_SPEED
            elif key == arcade.key.DOWN or key == arcade.key.S:
                self.player_sprite.change_y = -constants.PLAYER_MOVEMENT_SPEED
            elif key == arcade.key.LEFT or key == arcade.key.A:
                self.player_sprite.change_x = -constants.PLAYER_MOVEMENT_SPEED
            elif key == arcade.key.RIGHT or key == arcade.key.D:
                self.player_sprite.change_x = constants.PLAYER_MOVEMENT_SPEED
            
        if key == arcade.key.ENTER and self.show_text:
            self.show_battle_scene = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def update(self, delta_time):
        """ Movement and game logic """

        professor_collision = arcade.check_for_collision_with_list(self.player_sprite, self.professor_list)

        if len(professor_collision) > 0:
            self.show_text = True
        else:
            
            self.show_text = False

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