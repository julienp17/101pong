# -*-coding:Utf-8 -*
##
## EPITECH PROJECT, 2019
## 101pong
## File description:
## Main file for 101pong
##

from sys import argv, stderr, exit
from print_res import *
from vector import *
from constants import *
from help_option import *

if (is_help_option(argv)):
    print_description()
    exit(MY_EXIT_SUCCESS)
if (len(argv) != NB_ARGS):
    print(INVALID_NB_ARGS_MSG, file = stderr)
    exit(MY_EXIT_FAILURE)

try:
    x0 = float(argv[1])
    y0 = float(argv[2])
    z0 = float(argv[3])
    x1 = float(argv[4])
    y1 = float(argv[5])
    z1 = float(argv[6])
    n = int(argv[7])
except ValueError:
    print(INCORRECT_TYPE_MSG, file = stderr)
    exit(MY_EXIT_FAILURE)
if (n < 0):
    print(NEG_N_MSG, file = stderr)
    exit(MY_EXIT_FAILURE)

vector_1 = Vector(x0, y0, z0)
vector_2 = Vector(x1, y1, z1)
vel_vector = get_velocity_vector(vector_1, vector_2)
ball_coordinates = get_ball_coordinates(vector_1, vel_vector, n)

print_vel_vector(vel_vector)
print_ball_coordinates(ball_coordinates, n)