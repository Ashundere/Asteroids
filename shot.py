import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
	def __init__(self, position, velocity):
		super().__init__(position.x, position.y, SHOT_RADIUS)
		self.position = position
		self.velocity = velocity
	def draw(self, screen):
		pygame.draw.circle(screen, "red", self.position,SHOT_RADIUS,2)

	def update(self, dt):
                self.position += self.velocity * dt
