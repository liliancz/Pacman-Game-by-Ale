import pygame, sys
from settings import *
from player_class import *
from enemy_class import *

pygame.init()   
vec = pygame.math.Vector2

class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'
        self.cell_width = MAZE_WIDTH // 28
        self.cell_height = MAZE_HEIGHT // 30
        self.enemies = []
        self.walls =[]
        self.coins =[]
        self.enemies = []
        self.e_pos = []
        self.p_pos = None
        self.load()
        self.player = Player(self, self.p_pos)
        self.make_enemies()
        
    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            elif self.state =='play':
                self.play_events()
                self.play_update()
                self.play_draw()
            else:
                self.running = False
            self.clock.tick(FPS)            
        pygame.quit()
        sys.exit()

################### HELPFULL FUNCTIONS ##############


    def draw_text(self, displayed_text, screen, pos, size, colour, font_name,
                  centered=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(displayed_text, False, colour)
        text_size = text.get_size()
        if centered:
            pos[0]= pos[0]-text_size[0]//2
            pos[1]= pos[1]-text_size[1]//2
        screen.blit(text, pos)

    def load(self):
        self.background = pygame.image.load('background.png')
        self.background = pygame.transform.scale(self.background,
                                                 (MAZE_WIDTH, MAZE_HEIGHT))

        #Opening walls file
        #Creating walls list with co-ords of walls
        #stored as a vector
        with open("walls.txt", 'r') as file:
            for yindex, line in enumerate(file):
                for xindex, char in enumerate(line):
                    if char == "1":
                        self.walls.append(vec(xindex, yindex))
                    elif char == "C":
                        self.coins.append(vec(xindex, yindex))
                    elif char == "P":
                        self.p_pos = vec(xindex, yindex)
                    elif char in ["2","3","4","5"]:
                        self.e_pos.append(vec(xindex, yindex))
                    elif char == "B":
                        pygame.draw.rect(self.background, BLACK, (xindex*self.cell_width, yindex*self.cell_height, self.cell_width, self.cell_height))
                    
        
                        
    def make_enemies(self):
        for index, pos in enumerate(self.e_pos):
            self.enemies.append(Enemy(self, pos, index))

        
    def draw_grid(self):
        for x in range(WIDTH//self.cell_width):
            pygame.draw.line(self.background, GREY, (x*self.cell_width, 0),
                             (x*self.cell_width, HEIGHT))
        for x in range(HEIGHT//self.cell_height):
            pygame.draw.line(self.background, GREY, (0, x*self.cell_height),
                             (WIDTH, x*self.cell_height))
       # for wall in self.walls:
        #    pygame.draw.rect(self.background, (112, 55, 169),(wall.x*self.cell_width,
         #                   wall.y*self.cell_height, self.cell_width, self.cell_height))
       # for coin in self.coins:
        #    pygame.draw.rect(self.background, (10,150,20), (coin.x*self.cell_width,
         #                   coin.y*self.cell_height, self.cell_width, self.cell_height))

################### START FUNCTIONS #################
    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'play'
                

    def start_update(self):
        pass
    
    def start_draw(self):
        self.screen.fill(BLACK)
        self.draw_text('PUSH SPACE BAR', self.screen, [WIDTH//2, HEIGHT//2],
                       START_TEXT_SIZE, (170,132,58), START_FONT, centered=True)
        self.draw_text('1 PLAYER ONLY', self.screen, [WIDTH//2, HEIGHT//2+50],
                       START_TEXT_SIZE, (44,167,198), START_FONT, centered=True)
        self.draw_text('HIGH SCORE', self.screen, [WIDTH//2, 5],
                       START_TEXT_SIZE, WHITE, START_FONT, centered=True)
        pygame.display.update()

################### PLAY FUNCTIONS #################
    def play_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move(vec(-1,0))
                if event.key == pygame.K_RIGHT:
                    self.player.move(vec(1,0))
                if event.key == pygame.K_DOWN:
                    self.player.move(vec(0,1))
                if event.key == pygame.K_UP:
                    self.player.move(vec(0,-1))
           
                

    def play_update(self):
        self.player.update()
        for enemy in self.enemies:
            enemy.update()
    
    def play_draw(self):
        self.screen.fill(BLACK)

        self.screen.blit(self.background, (TOP_BOTTOM_BUFFER//2,
                                           TOP_BOTTOM_BUFFER//2))
        self.draw_coins()
        self.draw_grid()
        self.draw_text('SCORE : {}'.format(self.player.current_score), self.screen, [60,0], 16, WHITE,
                       START_FONT)
        self.draw_text('HIGH SCORE : 0', self.screen, [WIDTH//2+60,0], 16, WHITE,
                       START_FONT)
        self.player.draw()
        for enemy in self.enemies:
            enemy.draw()
        pygame.display.update()
        #self.coins.pop()

    def draw_coins(self):
        for coin in self.coins:
            pygame.draw.circle(self.screen, (82,120,25),
                               (int(coin.x*self.cell_width)+self.cell_width//2+TOP_BOTTOM_BUFFER//2,
                                int(coin.y*self.cell_height)+self.cell_height//2+TOP_BOTTOM_BUFFER//2),4)
        
    

    
