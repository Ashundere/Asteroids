from circleshape import CircleShape
from constants import *
from shot import Shot
import pygame

class Player(CircleShape):
	def __init__(self,x,y,radius):
		super().__init__(x,y,radius)
		self.x = x
		self.y = y
		self.radius = radius
		self.rotation = 0
		self.shoot_timer = 0
	# in the player class
	def triangle(self):
    		forward = pygame.Vector2(0, 1).rotate(self.rotation)
    		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    		a = self.position + forward * self.radius
    		b = self.position - forward * self.radius - right
    		c = self.position - forward * self.radius + right
    		return [a, b, c]

	def draw(self,screen):
		points =self.triangle()
		pygame.draw.polygon(screen,"white",points, 2)

	def rotate(self,dt):
		self.rotation += PLAYER_TURN_SPEED * dt
	
	def update(self,dt):
		keys = pygame.key.get_pressed()
		self.shoot_timer -= dt
		if keys[pygame.K_a]:
			self.rotate(-dt)
		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(-dt)
		if keys[pygame.K_SPACE]:
			self.shoot()

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt
	
	def shoot(self):
		if self.shoot_timer > 0:
			pass
		else:
			direction = pygame.Vector2(0, 1).rotate(self.rotation).normalize()
			shot_position = pygame.Vector2(self.position)
			offset = direction * (PLAYER_RADIUS + SHOT_RADIUS)
			shot_position += offset
			velocity = direction * PLAYER_SHOOT_SPEED
			Shot(shot_position, velocity)
			self.shoot_timer = PLAYER_SHOOT_COOLDOWN
