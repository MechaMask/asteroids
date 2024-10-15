import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot
class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0
    def draw(self,screen):
        pygame.draw.polygon(screen,"white",self.triangle(),2)
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def rotate(self, delta):
        self.rotation += PLAYER_TURN_SPEED * delta
    def move(self, delta):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * delta
    def shoot(self):
        if not (self.shot_timer > 0): 
            shot = Shot(self.position.x,self.position.y)
            shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shot_timer = PLAYER_SHOOT_COOLDOWN
    def update(self, delta):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_w]:
            self.move(delta)
        if keys[pygame.K_a]:
            self.rotate(-delta)
        if keys[pygame.K_s]:
            self.move(-delta)
        if keys[pygame.K_d]:
            self.rotate(delta)
        self.shot_timer -= delta
