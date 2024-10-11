import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from explosion import Explosion
import random

def main():
    
    # initialize pygame
    pygame.init()
    
    # game screen set up
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    
    # clock for FPS
    clock = pygame.time.Clock()
    dt = 0 # delta time
    
    score = 0
    lives = 5
    font = pygame.font.SysFont("Arial", 24)
    
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
    
    
    def reset_game(player, asteroids, shots, asteroid_field, updatable, drawable):
        # Reset player position and velocity
        player.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        player.velocity = pygame.Vector2(0, 0)

        # Clear asteroids, shots, and temporarily stop spawning
        asteroid_field.reset(asteroids, updatable, drawable)
        shots.empty()  # Clear all shots

        # After a delay, re-enable asteroid spawning
        pygame.time.set_timer(pygame.USEREVENT + 1, 1500)  # 1.5 second delay to enable spawning

    
    
    
    
    # Game loop
    while True:
        
        # handling events (+ check for quit)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.USEREVENT + 1:
                asteroid_field.enable_spawning()  # Re-enable spawning after the reset delay
        
        
        dt = clock.tick(60) / 1000 # milliseconds to seconds // fps = 60
        screen.fill((0,0,0))
        
        for obj in drawable:
            obj.draw(screen)
    
        # Render the score on the screen
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))  # White text
        lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255)) 
        screen.blit(score_text, (10, 10))  # Display the score in the top-left corner
        screen.blit(lives_text, (10, 40)) 
        
        # refresh screen for changes
        pygame.display.flip()
        
        for obj in updatable:
            obj.update(dt)
        
        # check for collisions
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                lives -= 1
                if lives > 0:
                    
                    # Respawn the player if lives remain
                    reset_game(player, asteroids, shots, asteroid_field, updatable, drawable)

                    
                    print(f"Lives left: {lives}")
                    
                    # Dim the background 
                    dim_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
                    dim_surface.set_alpha(128)  # 50% opacity
                    dim_surface.fill((0, 0, 0))  # Black color
                    screen.blit(dim_surface, (0, 0)) 
                    
                    # Display "Lives Left"
                    lives_left_text = font.render(f"Lives Left: {lives}", True, (255, 0, 0))  # Red text for lives left
                    screen.blit(lives_left_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
                    pygame.display.flip()
                    pygame.time.wait(1500)  # Pause for 1.5 seconds to show the message
                    
                else:
                    print(f"Score: {score}")
                    print("Game over!")
                    
                    
                    # Dim the background 
                    dim_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
                    dim_surface.set_alpha(128)  # 50% opacity
                    dim_surface.fill((0, 0, 0))  # Black color
                    screen.blit(dim_surface, (0, 0)) 
                    
                    # Display "Game Over"
                    game_over_text = font.render("Game Over!", True, (255, 0, 0))  # Red text for game over
                    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
                    pygame.display.flip()
                    pygame.time.wait(3000)  # Pause for 3 seconds before quitting
                    pygame.quit()
                    return
            
            # check collision with shots
            for shot in shots:
                if asteroid.collides_with(shot):
                    # remove shot and split asteroid
                    asteroid.split()
                    shot.kill()
                    
                    # Trigger the explosion at the asteroid's position
                    explosion = Explosion(asteroid.position.x, asteroid.position.y, max_radius=50)
                    drawable.add(explosion)
                    updatable.add(explosion)
                    
                    score += 1
            
                    break

        asteroid_field.update(dt)


if __name__ == "__main__":
    main()
