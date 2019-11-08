# -*-coding:Utf-8 -*
##
## EPITECH PROJECT, 2019
## 101pong
## File description:
## Unit tests for the help option
##

"This file contains unit tests for the help option of the 101pong program"

import sys
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from src.help_option import *

class TestHelpOption(TestCase):

    """Unit test class of the help option.

    Test the output to the console.

    """

    def test_is_help_option_bad_ac(self):

        argv = ["./101pong", "-h", "yeyy"]
        self.assertFalse(is_help_option(argv))
        argv = ["./101pong"]
        self.assertFalse(is_help_option(argv))

    def test_is_help_option_bad_option(self):

        argv = ["./101pong", "-o"]
        self.assertFalse(is_help_option(argv))
        argv = ["./101pong", "42"]
        self.assertFalse(is_help_option(argv))
        argv = ["./101pong", "this is a string"]
        self.assertFalse(is_help_option(argv))

    def test_is_help_option_true(self):

        argv = ["./101pong", "-h"]
        self.assertTrue(is_help_option(argv))
        argv = ["./101pong", "--help"]
        self.assertTrue(is_help_option(argv))

    def test_print_usage(self):

        expected = "USAGE\n" + "    ./101pong x0 y0 z0 x1 y1 z1 n\n"
        with patch("sys.stdout", new = StringIO()) as mock_stdout:
            print_usage()
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_print_description(self):

        expected =  "USAGE\n"
        expected += "    ./101pong x0 y0 z0 x1 y1 z1 n\n"
        expected += "\n"
        expected += "DESCRIPTION\n"
        expected += "    x0  ball abscissa at time t - 1\n"
        expected += "    y0  ball ordinate at time t - 1\n"
        expected += "    z0  ball altitude at time t - 1\n"
        expected += "    x1  ball abscissa at time t\n"
        expected += "    y1  ball ordinate at time t\n"
        expected += "    z1  ball altitude at time t\n"
        expected += "    n   time shift (greater than or equal to zero, "
        expected += "integer)\n"
        with patch("sys.stdout", new = StringIO()) as mock_stdout:
            print_description()
            self.assertEqual(mock_stdout.getvalue(), expected)