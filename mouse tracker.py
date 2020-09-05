import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800,600))

while True:
	for event in pygame.event.get():
		print(event)

		if event.type == pygame.QUIT:
			sys.exit()
