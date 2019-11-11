# -*-coding:Utf-8 -*
##
## EPITECH PROJECT, 2019
## 101pong
## File description:
## Functions to display the game
##

import pygame
from classes.Paddle import Paddle
from classes.Ball import Ball
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

def display_ball(ball: Ball):
    pygame.draw.rect(ball.image, WHITE, [0, 0, ball.width, ball.height])

def display_score(screen, score_left: int, score_right: int):
    font = pygame.font.Font(None, SCORE_FONT_SIZE)
    text = font.render(str(score_left), 1, WHITE)
    screen.blit(text, (int(W_WIDTH / 4), 20))
    text = font.render(str(score_right), 1, WHITE)
    screen.blit(text, (int(W_WIDTH * 3 / 4), 20))

def display_ball_trajectory(screen, ball: Ball):
    x_beg = ball.rect.x + ball.width / 2
    y_beg = ball.rect.y + ball.height / 2
    pos_beg = [x_beg, y_beg]
    x_end = ball.rect.x + (ball.vx * 100)
    y_end = ball.rect.y + (ball.vy * 100)
    pos_end = [x_end, y_end]
    pygame.draw.line(screen,
                    GREEN,
                    pos_beg,
                    pos_end,
                    3)

def display_ball_movement_equations(screen, ball: Ball):
    text_x = int(ball.rect.x + 20)
    text_y = int(ball.rect.y - 80)
    text_pos = (text_x, text_y)
    font = pygame.font.Font(None, 25)
    text = font.render("ball x : " + str(ball.rect.x), 1, WHITE)
    screen.blit(text, text_pos)
    text_y += 20
    text_pos = (text_x, text_y)
    text = font.render("ball y : " + str(ball.rect.y), 1, WHITE)
    screen.blit(text, text_pos)
    text_y += 20
    text_pos = (text_x, text_y)
    text = font.render("ball vx : " + str(ball.vx), 1, WHITE)
    screen.blit(text, text_pos)
    text_y += 20
    text_pos = (text_x, text_y)
    text = font.render("ball vy : " + str(ball.vy), 1, WHITE)
    screen.blit(text, text_pos)