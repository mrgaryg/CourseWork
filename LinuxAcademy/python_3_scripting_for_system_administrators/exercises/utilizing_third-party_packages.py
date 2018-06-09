#!/usr/bin/env python
# https://linuxacademy.com/cp/exercises/view/id/715/module/168
# Make sure that you have the requests package installed. Now, write a script that does the following:
# Accepts a URL and destination file name from the user calling the script.
# Utilizes requests to make an HTTP request to the given URL.
# Has an optional flag to state whether or not the response should be JSON or HTML (HTML by default).
# Writes the contents of the page out to the destination.
# Note: You’ll want to use the text attribute to get the HTML.

import os
import sys
import requests
from argparse import ArgumentParser

# Accepts a URL and destination file name from the user calling the script.
parser = ArgumentParser(description="Takes a URL, and downloads it's contents/response into a specified files. Allows user to specify output to be stored as JSON. Default output format is HTML.")
parser.add_argument('url', help='the URL to fetch')
parser.add_argument('filename', help='the name of the file')
# Has an optional flag to state whether or not the response should be JSON or HTML (HTML by default).
parser.add_argument('-j', '--json', action='store_true', help="change output to json" )

args = parser.parse_args()
url = args.url
filename = args.filename
isjson = args.json
if isjson:
    print (f"Format will be JSON")
    # oformat = 'html'
else:
    print ("Format will be HTML") 

# Utilizes requests to make an HTTP request to the given URL.
res = requests.get(url)

if ConnectionError != 200:
    print (f"ERROR: Connecting to address specified: {res}")
    sys.exit(1)

# TODO: Make it work with this method later
# try:
#     res = requests.get(url)
# except ConnectionError:
#     print (f"ERROR: invalid address specified {res}")
#     sys.exit(1)
# except requests.exceptions.HTTPError as err:
#     print (f"ERROR: site responded with {err}")
#     sys.exit(1)
# else:
#     print (f"Site responded with code {res.status_code}")
#     # print(res)

sys.exit (0)
# Writes the contents of the page out to the destination.
file_output = []
with open(filename, mode='w') as f:
    print (f"Contents will be written to {filename}")
    for line in file_output:
        f.write(line + "\n")    

# Note: You’ll want to use the text attribute to get the HTML.
