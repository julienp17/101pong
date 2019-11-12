#!/usr/bin/python3
# -*-coding:Utf-8 -*

##
## EPITECH PROJECT, 2019
## 101pong
## File description:
## Main file for pong game in pygame
##

import pygame
import time
from classes.Paddle import Paddle
from classes.Ball import Ball
from src.constants import *
from src.display import *

pygame.init()
pygame.mixer.init()
w_size = (W_WIDTH, W_HEIGHT)
screen = pygame.display.set_mode(w_size, pygame.FULLSCREEN)
pygame.display.set_caption(W_TITLE)
pygame.mixer.music.load("assets/audio/elevator.wav")
goal_sound = pygame.mixer.Sound("assets/audio/coin.wav")
nice = pygame.mixer.Sound("assets/audio/nice.wav")
#pygame.mixer.music.play(0)

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
    move_left_paddle(keys, left_paddle)
    move_right_paddle(keys, right_paddle)

def move_left_paddle(keys: list, left_paddle: Paddle):
    if keys[pygame.K_a]:
        left_paddle.move_up(PADDLE_MOVE_PIXELS)
    if keys[pygame.K_q]:
        left_paddle.move_down(PADDLE_MOVE_PIXELS)

def move_right_paddle(keys: list, right_paddle: Paddle):
    if keys[pygame.K_UP]:
        right_paddle.move_up(PADDLE_MOVE_PIXELS)
    if keys[pygame.K_DOWN]:
        right_paddle.move_down(PADDLE_MOVE_PIXELS)

clock = pygame.time.Clock()
pygame.key.set_repeat(0, 500)
game_on = True
game_is_paused = False
while (game_on):
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if (event.type == pygame.QUIT):
            game_on = False
        if (keys[pygame.K_ESCAPE]):
            game_on = False
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_SPACE]):
        if (game_is_paused == False):
            game_is_paused = True
        else:
            game_is_paused = False
    if (game_is_paused == False):
        move_paddles(keys, left_paddle, right_paddle)
        ball.check_bounce(left_paddle, right_paddle)
        if (ball.rect.x <= 0):
            score_right += 1
            ball.reset_ball()
            goal_sound.play(0)
        if (ball.rect.x + ball.width >= W_WIDTH):
            score_left += 1
            ball.reset_ball()
            goal_sound.play(0)
        if (score_left == 6 and score_right == 9):
            nice.play(0)
        sprites_list.update()
        screen.fill(BLACK)
        sprites_list.draw(screen)
        display_middle_line(screen, NB_LINES_MIDDLE)
        display_paddles(left_paddle, right_paddle)
        display_ball(ball)
        display_score(screen, score_left, score_right)
        ball.update_speed()
    else:
        display_ball_trajectory(screen, ball)
        display_ball_movement_equations(screen, ball)
    pygame.display.flip()
    clock.tick(FPS_LIMIT)
pygame.quit()