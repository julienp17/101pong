# -*-coding:Utf-8 -*
##
## EPITECH PROJECT, 2019
## 101pong
## File description:
## Contains constants for 101pong pygame
##

"""This file contains all constants of 101pong."""

from random import randint

MY_EXIT_SUCCESS             =       0
MY_EXIT_FAILURE             =       84
NB_ARGS                     =       8

BLACK                       =       (0, 0, 0)
WHITE                       =       (255, 255, 255)
RED                         =       (255, 0, 0)
GREEN                       =       (0, 255, 0)
BLUE                        =       (0, 0, 255)

W_WIDTH                     =       800
W_HEIGHT                    =       600
W_TITLE                     =       "My Pong"
FRAMERATE                   =       60

BALL_WIDTH                  =       10
BALL_HEIGHT                 =       10
BALL_SPAWN_X                =       int((W_WIDTH - BALL_WIDTH) / 2)
BALL_SPAWN_Y                =       int((W_HEIGHT - BALL_HEIGHT) / 2)
BALL_SPAWN_VX               =       3
BALL_SPAWN_VY               =       3

PADDLE_WIDTH                =       10
PADDLE_HEIGHT               =       80
PADDLE_MOVE_PIXELS          =       10

NB_LINES_MIDDLE             =       12
SCORE_FONT_SIZE             =       60