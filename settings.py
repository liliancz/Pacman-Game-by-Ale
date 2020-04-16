from pygame.math import Vector2 as vec

# screen settings
TOP_BOTTOM_BUFFER = 50
WIDTH, HEIGHT = 610, 670
MAZE_WIDTH, MAZE_HEIGHT = WIDTH-TOP_BOTTOM_BUFFER, HEIGHT-TOP_BOTTOM_BUFFER
FPS = 60
COLS = 28
ROWS = 30
# colour settings
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREY = (107, 107, 107)
PLAYER_COLOUR = (150, 150, 0) 

# font settings
START_TEXT_SIZE = 16
START_FONT = 'arial black'
OVER_TEXT_SIZE = 16

# player settings
#PLAYER_START_POS = vec(13,17)
