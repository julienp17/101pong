# -*-coding:Utf-8 -*
##
## EPITECH PROJECT, 2019
## 101pong
## File description:
## Main file for 101pong
##

from sys import argv, exit
from print_res import *
from vector import *
from constants import *
from options import *

if (is_help_option(argv)):
    print_description()
    exit(MY_EXIT_SUCCESS)
if (len(argv) != NB_ARGS):
    print(INVALID_NB_ARGS_MSG)
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
    print(INCORRECT_TYPE_MSG)
    exit(MY_EXIT_FAILURE)
if (n < 0):
    print(NEG_N_MSG)
    exit(MY_EXIT_FAILURE)

vector_1 = Vector(x0, y0, z0)
vector_2 = Vector(x1, y1, z1)

vel_vector = get_velocity_vector(vector_1, vector_2)

print_vel_vector(vel_vector)
#print("x0 = %.2f" % x0)
#print("y0 = " + str(y0))
#print("z0 = " + str(z0))
#print("x1 = " + str(x1))
#print("y1 = " + str(y1))
#print("z1 = " + str(z1))
#print("n  = " + str(n))