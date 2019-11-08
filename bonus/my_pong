#!/usr/bin/python3
# -*-coding:Utf-8 -*

##
## EPITECH PROJECT, 2019
## 101pong
## File description:
## Main file for pong game in pygame
##

import pygame
from classes.Paddle import Paddle
from classes.Ball import Ball
from src.constants import *
from src.display import *

pygame.init()
w_size = (W_WIDTH, W_HEIGHT)
screen = pygame.display.set_mode(w_size)
pygame.display.set_caption(W_TITLE)

left_paddle = Paddle(0)
right_paddle = Paddle(W_WIDTH - PADDLE_WIDTH)
ball = Ball()

score_left = 0
score_right = 0

font = pygame.font.Font(None, 74)
sprites_list = pygame.sprite.Group()
sprites_list.add(left_paddle)
sprites_list.add(right_paddle)
sprites_list.add(ball)

def move_paddles(keys: list, left_paddle: Paddle, right_paddle: Paddle):
    if keys[pygame.K_a]:
        left_paddle.move_up(PADDLE_MOVE_PIXELS)
    if keys[pygame.K_q]:
        left_paddle.move_down(PADDLE_MOVE_PIXELS)
    if keys[pygame.K_UP]:
        right_paddle.move_up(PADDLE_MOVE_PIXELS)
    if keys[pygame.K_DOWN]:
        right_paddle.move_down(PADDLE_MOVE_PIXELS)

clock = pygame.time.Clock()
game_on = True
while (game_on):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            game_on = False
    keys = pygame.key.get_pressed()
    move_paddles(keys, left_paddle, right_paddle)
    ball.check_bounce(left_paddle, right_paddle)
    if (ball.rect.x <= 0):
        score_right += 1
        ball.reset_ball()
    if (ball.rect.x + ball.width >= W_WIDTH):
        score_left += 1
        ball.reset_ball()
    sprites_list.update()
    screen.fill(BLACK)
    sprites_list.draw(screen)
    display_middle_line(screen, NB_LINES_MIDDLE)
    display_paddles(left_paddle, right_paddle)
    pygame.draw.rect(ball.image, WHITE, [0, 0, ball.width, ball.height])
    text = font.render(str(score_left), 1, WHITE)
    screen.blit(text, (int(W_WIDTH / 4), 20))
    text = font.render(str(score_right), 1, WHITE)
    screen.blit(text, (int(W_WIDTH * 3 / 4), 20))
    pygame.display.flip()
    ball.update_speed()
    clock.tick(FPS_LIMIT)
pygame.quit()