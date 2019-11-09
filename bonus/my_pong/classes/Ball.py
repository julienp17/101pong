# -*-coding:Utf-8 -*
##
## EPITECH PROJECT, 2019
## 101pong
## File description:
## Containes the Ball class
##

import pygame
from classes.Paddle import Paddle
from src.constants import *

class Ball(pygame.sprite.Sprite):

    """This class represents a Ball in the traditionnal game Pong."""

    def __init__(self):
        # Calls the parent class Sprite constructer
        super().__init__()

        self.image = self.init_image_()
        self.width = BALL_WIDTH
        self.height = BALL_HEIGHT
        self.rect = self.image.get_rect()
        self.rect.x = int((W_WIDTH - BALL_WIDTH) / 2)
        self.rect.y = int((W_HEIGHT - BALL_HEIGHT) / 2)
        self.vx = randint(-BALL_SPAWN_RANDOM_VX, BALL_SPAWN_RANDOM_VX)
        self.vy = randint(-BALL_SPAWN_RANDOM_VY, BALL_SPAWN_RANDOM_VY)

    def init_image_(self):
        image = pygame.Surface([PADDLE_WIDTH, PADDLE_HEIGHT])
        image.fill(BLACK)
        image.set_colorkey(BLACK)
        return (image)

    def update_speed(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

    def bounce_wall(self):
        self.vy = -self.vy
        if (self.vy < 0):
            self.vy -= 1
        else:
            self.vy += 1

    def bounce_paddle(self):
        self.vx = -self.vx
        if (self.vx < 0 and self.vx - 1 < -PADDLE_WIDTH):
            self.vx -= 1
        elif (self.vx >= 0 and self.vx + 1 < PADDLE_WIDTH):
            self.vx += 1

    def check_bounce(self, left_paddle: Paddle, right_paddle: Paddle):
        if (self.rect.y <= 0 or self.rect.y + self.height >= W_HEIGHT):
            self.bounce_wall()
        if (pygame.sprite.collide_mask(self, left_paddle)):
            self.bounce_paddle()
        if (pygame.sprite.collide_mask(self, right_paddle)):
            self.bounce_paddle()

    def reset_ball(self):
        self.rect.x = int((W_WIDTH - BALL_WIDTH) / 2)
        self.rect.y = int((W_HEIGHT - BALL_HEIGHT) / 2)
        self.vx = BALL_SPAWN_RANDOM_VX
        self.vy = BALL_SPAWN_RANDOM_VY