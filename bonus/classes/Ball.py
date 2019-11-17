# -*-coding:Utf-8 -*
##
## EPITECH PROJECT, 2019
## 101pong
## File description:
## Containes the Ball class
##

import random
import pygame
from classes.Paddle import Paddle
from src.constants import *

class Ball(pygame.sprite.Sprite):

    """This class represents a Ball in the traditionnal game Pong."""

    def __init__(self):
        # Calls the parent class Sprite constructer
        super().__init__()

        self.image = self.init_image_()
        self.rect = self.image.get_rect()
        self.width = BALL_WIDTH
        self.height = BALL_HEIGHT
        self.rect.x = BALL_SPAWN_X
        self.rect.y = BALL_SPAWN_Y
        self.vx = random.choice((-BALL_SPAWN_VX, BALL_SPAWN_VX))
        self.vy = random.choice((-BALL_SPAWN_VY, BALL_SPAWN_VY))

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
        if (abs(self.vy) < PADDLE_WIDTH - 1):
            if (self.vy < 0):
                self.vy -= 1
            else:
                self.vy += 1
        if (abs(self.vx) < PADDLE_WIDTH - 1):
            if (self.vx < 0):
                self.vx -= 1
            else:
                self.vx += 1

    def bounce_paddle(self):
        self.vx = -self.vx
        if (abs(self.vy) < PADDLE_WIDTH - 1):
            if (self.vy < 0):
                self.vy -= 1
            else:
                self.vy += 1
        if (abs(self.vx) < PADDLE_WIDTH - 1):
            if (self.vx < 0):
                self.vx -= 1
            else:
                self.vx += 1

    def check_bounce(self, left_paddle: Paddle, right_paddle: Paddle):
        bounce_sound = pygame.mixer.Sound("assets/audio/spring.wav")
        if (self.rect.y <= 0 or self.rect.y + self.height >= W_HEIGHT):
            bounce_sound.play(0)
            self.bounce_wall()
        if (pygame.sprite.collide_mask(self, left_paddle)):
            bounce_sound.play(0)
            self.bounce_paddle()
        if (pygame.sprite.collide_mask(self, right_paddle)):
            bounce_sound.play(0)
            self.bounce_paddle()

    def reset_ball(self):
        self.rect.x = BALL_SPAWN_X
        self.rect.y = BALL_SPAWN_Y
        self.vx = random.choice((-BALL_SPAWN_VX, BALL_SPAWN_VX))
        self.vy = random.choice((-BALL_SPAWN_VY, BALL_SPAWN_VY))