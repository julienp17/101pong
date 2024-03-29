##
## EPITECH PROJECT, 2019
## 101pong
## File description:
## Manipulate vectors
##

import sys
sys.path.insert(1, "../")
from sys import stderr, exit
from math import sqrt, pow, acos, degrees
from src.constants import *
from classes import Vector

def get_velocity_vector(vector_1: Vector, vector_2: Vector):
    velocity_vector = Vector.Vector(0, 0, 0)
    velocity_vector.x = vector_2.x - vector_1.x
    velocity_vector.y = vector_2.y - vector_1.y
    velocity_vector.z = vector_2.z - vector_1.z
    return (velocity_vector)

def get_ball_coordinates(vector_1: Vector, vel_vector: Vector, t: int):
    ball_coordinates = Vector.Vector(0, 0, 0)
    ball_coordinates.x = vel_vector.x * (t + 1) + vector_1.x
    ball_coordinates.y = vel_vector.y * (t + 1) + vector_1.y
    ball_coordinates.z = vel_vector.z * (t + 1) + vector_1.z
    return (ball_coordinates)

def get_incidence_angle(vel_vector: Vector):
    paddle_vector = Vector.Vector(vel_vector.x, vel_vector.y, 0)
    vector_scale1 = get_vector_scale(vel_vector)
    vector_scale2 = get_vector_scale(paddle_vector)
    if (vector_scale1 == 0):
        return (0.0)
    scalar_product = vector_scale2 / vector_scale1
    return (degrees(acos(scalar_product)))

def get_vector_scale(vector: Vector):
    return float(sqrt(pow(vector.x, 2) + pow(vector.y, 2) + pow(vector.z, 2)))

def ball_reach_paddle(z1: float, z2: float):
    if (z1 == 0):
        return (False)
    if ((z1 > 0.0 and z2 > 0.0) or (z1 < 0.0 and z2 < 0.0)):
        if (abs(z1) > abs(z2)):
            return (True)
        else:
            return (False)
    else:
        return (True)
