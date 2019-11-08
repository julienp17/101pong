# -*-coding:Utf-8 -*
##
## EPITECH PROJECT, 2019
## 101pong
## File description:
## Print the results
##

import sys
sys.path.insert(1, "../")
from classes import Vector

def print_vel_vector(vector:Vector):
    print("The velocity vector of the ball is:")
    print("(", end = "")
    print("%.2f" % vector.x + ", ", end = "")
    print("%.2f" % vector.y + ", ", end = "")
    print("%.2f" % vector.z, end = "")
    print(")")

def print_ball_coordinates(ball_coordinates: Vector, t: int):
    print("At time t + " + str(t) + ", ball coordinates will be:")
    print("(", end = "")
    print("%.2f" % ball_coordinates.x + ", ", end = "")
    print("%.2f" % ball_coordinates.y + ", ", end = "")
    print("%.2f" % ball_coordinates.z, end = "")
    print(")")

def print_incidence_angle(incidence_angle: float):
    if (incidence_angle < 0.0 or incidence_angle > 90.0):
        print("The ball won’t reach the paddle.")
    else:
        print("The incidence angle is:")
        print("%.2f" % incidence_angle, "degrees")