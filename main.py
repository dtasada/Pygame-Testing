#!/usr/bin/env python3

import pygame
from sys import exit
pygame.init()

x = 800
y = 600

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption('CAPTION')
clock = pygame.time.Clock()
#test_font = pygame.font.Font('path/font.ttf')

#test_surface = pygame.image.load('path/image.png').convert_alpha()
test_rectangle = test_surface.get_rect(midbottom = (x,y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface,(x,y))
   # screen.blit(test_surface2,test_rectangle2)
	
    pygame.display.update()
    clock.tick(60)
