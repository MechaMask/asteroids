import pygame
from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    delta = 0
    clock =  pygame.time.Clock()
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(delta)

        #rendering
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        delta = clock.tick(60)/1000 #update delta time
        

if __name__ == "__main__":
    main()
