import argparse

import sys

args = sys.argv[1:]

if "-h" in args or "--help" in args:
    print("Program to print args.")
    print("Options")
    print(" -h, --help      Priny this help text")
    exit(0)


for arg in args:
    print(arg)