# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player



def main():
	pygame.init()
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	player = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2),PLAYER_RADIUS)
	dt = 0
	while pygame.get_init() == 1:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
       				 return
		pygame.Surface.fill(screen,"black")
		player.draw(screen)
		player.update(dt)
		pygame.display.flip()
		clock.tick(60)
		dt = (clock.tick(60) / 1000)
		
if __name__ == "__main__":
    main()
