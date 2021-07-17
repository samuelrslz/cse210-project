import os
# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Kevin: Divine Program Master"

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 1
TILE_SCALING = 0.5
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * TILE_SCALING)

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 0

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
LEFT_VIEWPORT_MARGIN = 300
RIGHT_VIEWPORT_MARGIN = 300
BOTTOM_VIEWPORT_MARGIN = 400
TOP_VIEWPORT_MARGIN = 400

PLAYER_START_X = 64
PLAYER_START_Y = 225

# PHILLIPS_START_X = 75 * SPRITE_PIXEL_SIZE/2
# PHILLIPS_START_Y = 70 * SPRITE_PIXEL_SIZE/2

PHILLIPS_START_X = 5 * SPRITE_PIXEL_SIZE/2
PHILLIPS_START_Y = 5 * SPRITE_PIXEL_SIZE/2

KIRA_X = 74 * SPRITE_PIXEL_SIZE/2
KIRA_Y = 52 * SPRITE_PIXEL_SIZE/2

TEXT_BOX_HEIGHT = 160

MUSIC_VOLUME = 0.5

# IMAGES

PATH = os.path.dirname(os.path.abspath(__file__))
MAIN_MENU = os.path.join(PATH, "..", "assets", "images", "screens", "main_screen.png")

KEVIN_STANDING = os.path.join(PATH, "..", "assets", "images", "kevin", "kevin_standing.png")
KEVIN_BATTLE = os.path.join(PATH, "..", "assets", "images", "kevin", "kevin_battle.png")

KIRA_IMG = os.path.join(PATH, "..", "assets", "images", "custom_tiles", "kira.png")

PHILLIPS_STANDING = os.path.join(PATH, "..", "assets", "images", "custom_tiles", "phillips.png")
PHILLIPS_BATTLE = os.path.join(PATH, "..", "assets", "images", "professors", "phillips.png")

MAP = os.path.join(PATH, "..", "assets", "maps", "byui.tmx")
MINI_MAP = os.path.join(PATH, "..", "assets", "maps", "map.png")

BATTLE_BACKGROUNDS = os.path.join(PATH, "..", "assets", "images", "battle_scenes", "battle_mc.png")

# MUSIC
MUSIC_PATH = os.path.join(PATH, "..", "assets", "music")
DUB_HUB = os.path.join(MUSIC_PATH, "dubHub.mp3")
HAPPY8_BIT = os.path.join(MUSIC_PATH, "happy8-bit.mp3")
POWERUP = os.path.join(MUSIC_PATH, "Powerup.mp3")
DIGESTIVE_BISCUIT = os.path.join(MUSIC_PATH, "digestiveBiscuit.mp3")
MEGALOVANIA = os.path.join(MUSIC_PATH, "Megalovania.mp3")
MOUNTAIN_TRAILS = os.path.join(MUSIC_PATH, "MountainTrails.mp3")
#  = os.path.join(MUSIC_PATH, ".mp3")

# Temple
# Machines
