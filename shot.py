import pygame
from circleshape import CircleShape 
from constants import *


class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.radius = SHOT_RADIUS
        self.velocity = velocity
        
    def draw(self, screen):
        # Draw the shot as a small circle
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        # Move the shot in a straight line by adding velocity * dt to its position
        self.position += self.velocity * dt
        
    