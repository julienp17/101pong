# -*-coding:Utf-8 -*
##
## EPITECH PROJECT, 2019
## 101pong
## File description:
## Containes the Paddle class
##

import pygame
from src.constants import *

class Paddle(pygame.sprite.Sprite):

    """This class represents a Paddle in the traditionnal game Pong."""

    def __init__(self, x):
        # Calls the parent class Sprite constructer
        super().__init__()

        self.image = pygame.Surface([PADDLE_WIDTH, PADDLE_HEIGHT])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = int((W_HEIGHT - PADDLE_HEIGHT) / 2)

    def move_up(self, pixels: int):
        if (self.rect.y - pixels >= 0):
            self.rect.y -= pixels

    def move_down(self, pixels: int):
        if (self.rect.y + self.height + pixels <= W_HEIGHT):
            self.rect.y += pixels