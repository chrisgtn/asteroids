import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    
    # initialize pygame
    pygame.init()
    
    # game screen set up
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    
    # clock for FPS
    clock = pygame.time.Clock()
    dt = 0 # delta time
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Player object
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # Player
    Player.containers = (updatable, drawable)
    player = Player(x, y)
    
    #instead of containers
    # updatable.add(player)
    # drawable.add(player)
    
    # Asteroids
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    
    # Shots
    Shot.containers = (shots, updatable, drawable)
    
    
    
    
    # Game loop
    while True:
        
        # handling events (+ check for quit)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(60) / 1000 # milliseconds to seconds // fps = 60
        screen.fill((0,0,0))
        
        for obj in drawable:
            obj.draw(screen)
    
        # refresh screen for changes
        pygame.display.flip()
        
        for obj in updatable:
            obj.update(dt)
        
        # check for collisions
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                pygame.quit()
                return
            
            # check collision with shots
            for shot in shots:
                if asteroid.collides_with(shot):
                    # remove shot and asteroid
                    asteroid.split()
                    shot.kill()
                    break




if __name__ == "__main__":
    main()
