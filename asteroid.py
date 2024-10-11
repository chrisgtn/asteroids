import pygame
from circleshape import CircleShape 
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
        # Override velocity 
        #self.velocity = pygame.Vector2(100, 100) # pixels per second
        
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        # Move the asteroid in a straight line based on velocity and dt
        self.position += self.velocity * dt
