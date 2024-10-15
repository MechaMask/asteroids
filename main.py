import pygame
from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    delta = 0
    clock =  pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)  

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #update objects
        for obj in updatable:
            obj.update(delta)

        #rendering
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        
        delta = clock.tick(60)/1000 #update delta time
        

if __name__ == "__main__":
    main()
