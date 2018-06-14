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
parser = ArgumentParser(description=
'''
Takes a filename and URL as command line argument. URL can also be set as a  
default value by seting it as an environment variable 'URL'. The URL will be
fetched in in an HTML format by default, unless JSON flag is passed as an option.
The output will be written to a file specified as a command line argument mentioned 
above.'''
)
parser.add_argument('--url', default=os.environ.get('URL', None), help='Set the URL to fetch')
parser.add_argument('filename', help='the name of the file')
# Has an optional flag to state whether or not the response should be JSON or HTML (HTML by default).
parser.add_argument('-j', '--json', action='store_true', help="change output to json" )

args = parser.parse_args()
url = args.url
filename = args.filename
isjson = args.json

# Utilizes requests to make an HTTP request to the given URL.
resp = requests.get(url)

if resp.status_code != 200:
    print (f"ERROR: Connecting to address specified: {resp}")
    sys.exit(1)

print (f"Site responded with code {resp.status_code}")
if isjson:
    print ("Output was requested to be printed in JSON format")
    print (resp.json())
else:
    print ("Output was requested to be printed in HTML format") 
    print (resp.text)

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

# sys.exit (0)
# Writes the contents of the page out to the destination.
file_output = []
with open(filename, mode='w') as f:
    print (f"Contents will be written to {filename}")
    for line in file_output:
        f.write(line + "\n")    

# Note: You’ll want to use the text attribute to get the HTML.
