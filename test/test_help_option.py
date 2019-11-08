# -*-coding:Utf-8 -*
##
## EPITECH PROJECT, 2019
## 101pong
## File description:
## Unit tests for the help option
##

"This file contains unit tests for the help option of the 101pong program"

import sys
from src.help_option import *
from unittest import TestCase

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