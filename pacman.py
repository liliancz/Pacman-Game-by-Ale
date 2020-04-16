import pygame, sys, time
from pygame.locals import *
import random

pygame.init()
screen_width = 626
screen_height = 316
window = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pac - Man by Alejandra Cruz')
p_cI = 1
p_nI = 3
p_x = 0
p_y = 0
cfv= 0
pacman = pygame.image.load("pacman32x32.png")
black = 0,0,0
direction = 0
keypressed = False
angle = 0
while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				direction = 'up'
				keypressed = True
			elif event.key == pygame.K_DOWN:
				direction = 'down'
				keypressed = True
			elif event.key == pygame.K_RIGHT:
				direction = 'right'
				keypressed = True
			elif event.key == pygame.K_LEFT:
				direction = 'left'
				keypressed = True
			else:
				direction = direction

	if direction  == 'up':
		p_y -= 1
	if direction == 'down':
		p_y += 1
	if direction == 'right':
		p_x += 1	
	if direction == 'left':
		p_x -= 1
		
	window.fill(black)
	window.blit(pacman, (p_x,p_y), (p_cI*32, 0, 32, 32))

	pygame.display.update()
	if cfv > 500:
		cfv = 0
		if p_cI > p_nI-1 :
			p_cI = 0
		p_cI += 1
	cfv += 1
	



