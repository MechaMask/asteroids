import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    delta = 0
    clock =  pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids,updatable,drawable)
    Shot.containers = (shots,updatable,drawable)
    AsteroidField.containers = (updatable) 
    asteroid_field = AsteroidField()

    Player.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)  
    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #update objects
        for obj in updatable:
            obj.update(delta)
        for asteroid in asteroids:
            if asteroid.collision_detected(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collision_detected(shot):
                    shot.kill()
                    asteroid.kill()
        #rendering
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        
        delta = clock.tick(FPS)/1000 #update delta time
        

if __name__ == "__main__":
    main()
