#!/usr/bin/env python3.6

# Exercise requirements: https://linuxacademy.com/cp/exercises/view/id/711/module/168
# Receives a file_name and line_number as command line parameters.
# Prints the specified line_number from file_name to the screen. The user will specify this as you would expect, not using zero as the first line.
# Make sure that you handle the following error cases by presenting the user with a useful message:
# The file doesn’t exist.
# The file doesn’t contain the line_number specified (file is too short).

import argparse
import sys
# Receives a file_name and line_number as command line parameters.
parser = argparse.ArgumentParser(description='Read a file in reverse upto a line number specified')
parser.add_argument('file_name', help='the file to read')
parser.add_argument('line_number', type=int, help='line number to read')

args = parser.parse_args()

# Prints the specified line_number from file_name to the screen. The user will specify this as you would expect, not using zero as the first line.
try:
    f = open(args.file_name)
    read_line = args.line_number
except FileNotFoundError as err:
    print(f"Error: {err}")
    sys.exit (2)
else:
    # Open file
    with f:
        print(f"The line number you want printed is: {read_line}")
        
        # Check if line number exsits
        lines = f.readlines()
        print(f"The number of lines in this file is: {len(lines)}")
        
        if read_line > len(lines):
            print(f"ERROR: File '{args.file_name}' only has '{len(lines)}' lines in it. Please set a line number appropriately")
            sys.exit (2)
        else:
            line = lines[read_line - 1]
            print(f"Line '{read_line}' in this file is: '{line.strip()}'")
