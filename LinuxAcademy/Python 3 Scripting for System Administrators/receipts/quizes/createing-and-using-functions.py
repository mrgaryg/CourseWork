#!/usr/bin/env python3.6

def gather_info():
    # Prompt the user for a message to echo
    message = input("What is your message? ")

    # Prompts the user for the number of times to repeat the message. If no response is given, then the count should default to 1.
    repeats = input("How many times do you want to repeat this message? ")
    # int(repeats)
    return (message, repeats)

# Defines a function that takes a message and count then prints the message that many times.
def printMessage (message, count):
    # print(f"You want to repeat it '{count}' times")
    while count > 0:
        print(f"{count}: Your message is: '{message}'")
        count -= 1

message, count = gather_info()
if count:
    count = int(count)
else:
    count = 1

printMessage(message, count)

