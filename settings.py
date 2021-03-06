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
PLAYER_COLOUR = (255, 255, 0) 
COIN_COLOUR = (254,184,198)

# font settings
START_TEXT_SIZE = 16
START_FONT = 'Bahnschrift'
OVER_TEXT_SIZE = 16
OVER_FONT = 'Bahnschrift'

# player settings
#PLAYER_START_POS = vec(13,17)

#coin settings
COIN_RADIUS = 3
