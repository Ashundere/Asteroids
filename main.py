# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	player = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2),PLAYER_RADIUS)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = updatable
	asteroid_field = AsteroidField()
	Shot.containers =(shots, updatable, drawable)
	while pygame.get_init() == 1:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
       				 return
		pygame.Surface.fill(screen,"black")
		for item in drawable:
			item.draw(screen)
		updatable.update(dt)
		for asteroid in asteroids:
            		if asteroid.collides_with(player):
                		print("Game over!")
                		sys.exit()
		for asteroid in asteroids:
			for shot in shots:
				if asteroid.collides_with(shot):
					asteroid.split()
					shot.kill()
		pygame.display.flip()
		clock.tick(60)
		dt = (clock.tick(60) / 1000)
		
if __name__ == "__main__":
    main()
