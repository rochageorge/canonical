#!/usr/bin/python

"""Debian Package Statistics CLI Tool"""

import argparse
import os
import sys

import ps_library as mylib

# Create the parser
my_parser = argparse.ArgumentParser(description='Shows the statistics from a debian mirror')

# Add the arguments
my_parser.add_argument('Arch', metavar='arch',  type=str,  help='architecture (amd64, arm64, mips etc.)')

# Execute the parse_args() method
args = my_parser.parse_args()

# creates a variable for the input
input_arg = args.Arch

# Calls the method, passing the inputed architecture as argument
mylib.main(input_arg)
