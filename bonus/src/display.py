# -*-coding:Utf-8 -*
##
## EPITECH PROJECT, 2019
## 101pong
## File description:
## Functions to display the game
##

import pygame
from classes.Paddle import Paddle
from src.constants import *

def display_middle_line(screen, nb_lines: int):
    beg = 0
    end = beg + int(W_HEIGHT / nb_lines) - 20
    for x in range(0, W_HEIGHT, int(W_HEIGHT / nb_lines)):
        pygame.draw.line(screen, WHITE, [W_WIDTH / 2, beg], [W_WIDTH /2, end], 1)
        beg = end + 20
        end = beg + int(W_HEIGHT / nb_lines) - 20

def display_paddles(left_paddle: Paddle, right_paddle: Paddle):
    pygame.draw.rect(left_paddle.image, WHITE, [0, 0, left_paddle.width, left_paddle.height])
    pygame.draw.rect(right_paddle.image, WHITE, [0, 0, right_paddle.width, right_paddle.height])