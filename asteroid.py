import pygame
from circleshape import CircleShape 
from constants import *
import random


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
    
    def split(self):
        self.kill()
       
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        
        #new velocities (by rotation) + new radius
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # new asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        # scale up velocities
        asteroid1.velocity = velocity1 * 1.2
        asteroid2.velocity = velocity2 * 1.2