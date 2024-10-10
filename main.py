import pygame
from constants import *
from player import Player

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
    
    # Player object
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    Player.containers = (updatable, drawable)
    player = Player(x, y)
    
    #instead of containers
    # updatable.add(player)
    # drawable.add(player)
    
    
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

        




if __name__ == "__main__":
    main()
