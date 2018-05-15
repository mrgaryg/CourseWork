#!/usr/bin/env python3.6
# https://linuxacademy.com/cp/exercises/view/id/712/module/168
# 
# It’s not uncommon for a process to run on a server and listen to a port. Unfortunately, you sometimes don’t want that process 
# to keep running, but all you know is the port that you want to free up. You’re going to write a script to make it easy to get 
# rid of those pesky processes.
# Write a script that does the following:
# 
# * Takes a port_number as its only argument.
# * Calls out to lsof to determine if there is a process listening on that port.
# * If there is a process, kill the process and inform the user.
# * If there is no process, print that there was no process running on that port.
# 
# Python’s standard library comes with an HTTP server that you can use to start a server listening on a port (5500 in this case) with this line:
# $ python -m SimpleHTTPServer 5500
# 
# Use a separate terminal window/tab to test our your script to kill that process.
# 
# Hints:
# You may need to install lsof. Use this command on CentOS:
# $ sudo yum install -y lsof
# Use this line of lsof to get the port information:
# lsof -n -i4TCP:PORT_NUMBER
# That will return multiple lines, and the line you want will contain “LISTEN”.
# Use the string split() method to break a string into a list of its words.
# You can either use the kill command outside of Python or the os.kill(pid, 9) function.

import os
import argparse
import sys
import subprocess
# * Takes a port_number as its only argument.
parser = argparse.ArgumentParser(description="enter port number of the process")
parser.add_argument('port_number', help='specify port number')

args = parser.parse_args()
portnum = args.port_number

# print(args.port_number)
print(f"Checking for process running on port: {portnum}")

# * Calls out to lsof to determine if there is a process listening on that port.
myproc = subprocess.run(['lsof', '-n', f'-i4TCP:{portnum}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# * If there is a process, kill the process and inform the user.
if myproc.returncode == 0:
    procstr = myproc.stdout.decode().splitlines()
    prochead = procstr[0].split()
    procval = procstr[1].split()
    procdict = dict(zip(prochead,procval))
    procpid = int(procdict['PID'])
    # print(prochead, '\n', procval, '\n', procdict)
    print(f"Found a process running on port {portnum}")
    print(f"PID is: {procpid}")
    print("Time to die")
    os.kill(procpid, 9)

# * If there is no process, print that there was no process running on that port.
if myproc.returncode == 1:
    print(f"Did not find a process running on port {portnum}")
