#!/usr/bin/env python3
##
## EPITECH PROJECT, 2019
## unit test
## File description:
## unit test for "print_incidence angle"
##

"This file contains unit tests for the help option of the 101pong program"

import sys
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from src.print_res import *
from classes import Vector

class TestWontReachPaddle(TestCase):


    def test_print_incidence_angle_true(self):

        ball_reach = True
        incidence_angle = 15.5
        expected = "The incidence angle is:\n" + "15.50 degrees\n"
        with patch("sys.stdout", new = StringIO()) as mock_stdout:
            print_incidence_angle(ball_reach, incidence_angle)
            self.assertEqual(mock_stdout.getvalue(), expected)

    def	test_print_incidence_angle_false(self):

        ball_reach = False
        incidence_angle = 15.5
        expected = "The ball won't reach the paddle.\n"
        with patch("sys.stdout", new = StringIO()) as mock_stdout:
            print_incidence_angle(ball_reach, incidence_angle)
            self.assertEqual(mock_stdout.getvalue(), expected)


    def test_print_vel_vector(self):

        vector = Vector.Vector(6.00, 6.00, -7.00)
        expected = "The velocity vector of the ball is:\n" + "(6.00, 6.00, -7.00)\n"
        with patch("sys.stdout", new = StringIO()) as mock_stdout:
            print_vel_vector(vector)
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_print_vel_vector(self):

        ball_coordinates = Vector.Vector(31.00, 33.00, -30.00)
        t = 4
        expected = "At time t + 4, ball coordinates will be:\n" + "(31.00, 33.00, -30.00)\n"
        with patch("sys.stdout", new = StringIO()) as mock_stdout:
            print_ball_coordinates(ball_coordinates, t)
            self.assertEqual(mock_stdout.getvalue(), expected)
