# -*-coding:Utf-8 -*
##
## EPITECH PROJECT, 2019
## 101pong
## File description:
## Print the results
##

from vector import *

def print_vel_vector(vector:Vector):
    print("The velocity vector of the ball is :")
    print("(", end = "")
    print("%.2f" % vector.x + ", ", end = "")
    print("%.2f" % vector.y + ", ", end = "")
    print("%.2f" % vector.z, end = "")
    print(")")