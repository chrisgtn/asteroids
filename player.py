import pygame  # Import pygame because it will be used
from circleshape import CircleShape  # Import CircleShape from circleshape.py
from constants import *
from shot import Shot




class Player(CircleShape):
    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.player_radius = PLAYER_RADIUS
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
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2) # screen obejct, color, [] points, width
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        # decrese shoot timer by dt 
        if self.shoot_timer > 0:
            self.shoot_timer -= dt 
        
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt) # rotate left (counter-clockwise)
            
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt) # rotate right (clockwise)
            
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)
        
        if keys[pygame.K_SPACE]:
            self.shoot()
            
            
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    def shoot(self):
        
        if self.shoot_timer <= 0:
            shot_direction = pygame.Vector2(0, 1).rotate(self.rotation)  # Rotate to match player’s direction
            shot_velocity = shot_direction * PLAYER_SHOOT_SPEED  # Scale it up for shoot speed
            shot = Shot(self.position.x, self.position.y, shot_velocity)
            
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN