import pygame
from time import sleep

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, constraint, speed):
        super().__init__()
        self.image = pygame.image.load('graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        self.speed = speed
        self.max_x_constraint = constraint
        self.shoot_ready = True
        self.move_ready = True
        self.laser_time = 0
        self.move_time = 0
        self.cooldown = 600

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and self.move_ready:
            self.rect.x += self.speed
            self.move_ready = False
            self.move_time = pygame.time.get_ticks()
            
        elif keys[pygame.K_LEFT] and self.move_ready:
            self.rect.x -= self.speed
            self.move_ready = False
            self.move_time = pygame.time.get_ticks()

        
        if keys[pygame.K_SPACE] and self.shoot_ready:
            self.shoot_laser()
            self.shoot_ready = False
            self.laser_time = pygame.time.get_ticks()
    
    def recharge(self):
        if not self.shoot_ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.cooldown:
                self.shoot_ready = True
        if not self.move_ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.move_time >= self.cooldown:
                self.move_ready = True

    def shoot_laser(self):
        print("laser")

    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint

    def update(self):
        self.get_input()
        self.constraint()
        self.recharge()