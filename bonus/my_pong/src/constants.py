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

W_WIDTH                     =       800
W_HEIGHT                    =       600
W_TITLE                     =       "My Pong"
FPS_LIMIT                   =       60

BALL_WIDTH                  =       10
BALL_HEIGHT                 =       10
BALL_SPAWN_RANDOM_VX        =       3
BALL_SPAWN_RANDOM_VY        =       3

PADDLE_WIDTH                =       10
PADDLE_HEIGHT               =       80
PADDLE_MOVE_PIXELS          =       5

NB_LINES_MIDDLE             =       12

INVALID_NB_ARGS_MSG         =       "Invalid number of arguments"
INCORRECT_TYPE_MSG          =       "A parameter is not of correct type"
NEG_N_MSG                   =       "N must be greater or equal to zero"
DIVISION_BY_ZERO_MSG        =       "Division by zero"