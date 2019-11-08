##
## EPITECH PROJECT, 2019
## 101pong
## File description:
## Manipulate vectors
##

import sys
sys.path.insert(1, "../")
from math import sqrt, pow, acos, degrees
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
    normal_vector1 = get_normal_vector(vel_vector)
    normal_vector2 = get_normal_vector(paddle_vector)
    scalar_product = get_scalar_product(normal_vector1, normal_vector2)
    return (degrees(acos(scalar_product)))

def get_scalar_product(normal_vector1:Vector, normal_vector2: Vector):
    product = normal_vector1.x * normal_vector2.x
    product += normal_vector1.y * normal_vector2.y
    product += normal_vector1.z * normal_vector2.z
    return (product)

def get_normal_vector(vector: Vector):
    normal_vector = Vector.Vector(0, 0, 0)
    vector_scale = get_vector_scale(vector)
    normal_vector.x = vector.x / vector_scale
    normal_vector.y = vector.y / vector_scale
    normal_vector.z = vector.z / vector_scale
    return (normal_vector)

def get_vector_scale(vector: Vector):
    return float(sqrt(pow(vector.x, 2) + pow(vector.y, 2) + pow(vector.z, 2)))