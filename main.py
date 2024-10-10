import pygame
from constants import *

def main():
    
    # initialize pygame
    pygame.init()
    
    # game screen set up
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Game loop
   
    while True:
        
        # handling events (+ check for quit)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # fill screen RGB
        screen.fill((0,0,0))
    
        # refresh screen for changes
        pygame.display.flip()
        





if __name__ == "__main__":
    main()
