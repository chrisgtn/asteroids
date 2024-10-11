import pygame
import random
from asteroid import Asteroid
from constants import *


class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0
        self.can_spawn = True
        
    def spawn(self, radius, position, velocity):
        if not self.can_spawn:  # Prevent spawning when respawning
            return
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        if not self.can_spawn:  # Don't update or spawn new asteroids if respawning
            return
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)
            
    def reset(self, asteroids, updatable, drawable):
        """Reset asteroid field and clear all groups containing asteroids"""
        self.spawn_timer = 0  # Reset the spawn timer
        self.can_spawn = False  # Disable asteroid spawning temporarily

        # Clear all groups that may contain asteroids
        asteroids.empty()
        for asteroid in list(updatable):
            if isinstance(asteroid, Asteroid):
                asteroid.kill()

        for asteroid in list(drawable):
            if isinstance(asteroid, Asteroid):
                asteroid.kill()

    def enable_spawning(self):
        """Re-enable asteroid spawning after a delay"""
        self.can_spawn = True