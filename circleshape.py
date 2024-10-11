import pygame



"""CircleShape extends the Sprite class to also store a position, velocity, and radius.
Later you'll write subclasses of CircleShape and override the draw and 
update methods with the logic for that particular game object."""




# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    def collides_with(self, other):
        return self.position.distance_to(other.position) < self.radius + other.radius