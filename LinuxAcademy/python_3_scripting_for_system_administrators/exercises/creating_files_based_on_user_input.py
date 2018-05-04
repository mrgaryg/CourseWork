#!/usr/bin/env python3.6

# Exercise requirements: https://linuxacademy.com/cp/exercises/view/id/710/module/168
# Write a script that prompts the user for:
#   * A file_name where it should write the content.
#   * The content that should go in the file. The script should keep accepting lines of text until the user enters an empty line.
# After the user enters an empty line, write all of the lines to the file and end the script.

import os
import sys

# Read user input for file name
while True: 
    file_name = input("Specify file name for input\n> ")
    if os.path.isfile(file_name):
        print(f"file {file_name} exists. Try a different name.")
    else:
        print (f"Contents will be written to '{file_name}'")
        break

# Read in users content
file_output=[]
while True:
    user_input = input("Enter the text you want stored or press 'Enter' to exit\n> ").strip()
    # Check for empty line to exit
    if user_input == '':
        print(f"Enter key detected... Sending output to: '{file_output}'")
        break
    else:
        file_output.append(user_input)

with open(file_name, mode='w') as f:
    print (f"Contents will be written to {file_name}")
    for line in file_output:
        f.write(line + "\n")

# Exit script
print(f"File {file_name} written successfuly")
sys.exit(0)