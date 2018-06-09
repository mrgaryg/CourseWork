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
parser = ArgumentParser()
parser.add_argument('url', help='the URL to fetch')
parser.add_argument('filename', help='the name of the file')

args = parser.parse_args()

url = args.url
filename = args.filename

# Utilizes requests to make an HTTP request to the given URL.
try:
    res = requests.get(url)
except ConnectionError:
    print(f"ERROR: invalid address specified {res}")
    sys.exit(1)
except requests.exceptions.HTTPError as err:
    print(f"ERROR: site responded with {err}")
    sys.exit(1)
else:
    print (f"Site responded with code {res.status_code}")
    # print(res)
# Has an optional flag to state whether or not the response should be JSON or HTML (HTML by default).


# Writes the contents of the page out to the destination.
# Note: You’ll want to use the text attribute to get the HTML.
