import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, max_radius, color=(255, 255, 0)):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = 1  # Initial radius of the explosion
        self.max_radius = max_radius  # Maximum size the explosion will reach
        self.color = color 
        self.expansion_speed = 100 

    def update(self, dt):
        # Increase the radius of the explosion
        self.radius += self.expansion_speed * dt

        # If the explosion has reached its max size, kill the sprite
        if self.radius >= self.max_radius:
            self.kill()

    def draw(self, screen):
        # Draw the expanding explosion (fading red color as it grows)
        if self.radius < self.max_radius:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.radius), 2)
