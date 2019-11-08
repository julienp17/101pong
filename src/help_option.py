# -*-coding:Utf-8 -*
##
## EPITECH PROJECT, 2019
## 101pong
## File description:
## Handles options
##

def is_help_option(argv):
    if (len(argv) == 2 and (argv[1] == '-h' or argv[1] == '--help')):
        return True
    return False

def print_usage():
    print("USAGE")
    print("    ./101pong x0 y0 z0 x1 y1 z1 n")

def print_description():
    print_usage()
    print()
    print("DESCRIPTION")
    print("    x0  ball abscissa at time t-1")
    print("    y0  ball ordinate at time t-1")
    print("    z0  ball altitude at time t-1")
    print("    x1  ball abscissa at time t-1")
    print("    y1  ball ordinate at time t-1")
    print("    z1  ball altitude at time t-1")
    print("    n   time shift (greater than or equal to zero, integer")
