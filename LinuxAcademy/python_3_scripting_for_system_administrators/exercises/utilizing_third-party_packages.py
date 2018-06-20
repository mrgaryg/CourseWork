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
import json
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

# The following argument line was brought over from the official answer
# It's non-functional, and is here only for reference
parser.add_argument('-c', '--content-type',
                    default='html',
                    choices=['html', 'json'],
                    help="change output to json" )

args = parser.parse_args()
url = args.url
filename = args.filename
isjson = args.json

print (">Param settings are:")
print (f"~The URL requested is: {url}")
print (f"~The contents will be written to {filename}")

# Utilizes requests to make an HTTP request to the given URL.
resp = requests.get(url, stream=True)

if resp.status_code >= 400:
    print (f"~! ERROR Connecting to address specified: {resp.status_code}")
    sys.exit(1)

print (f"~Site responded with code {resp.status_code}")

if isjson:
    print ("~Content-type is specified as JSON format")
    # print (resp.json())
    try:
        content = json.dumps(resp.json())
    except ValueError:
        print ('~! ERROR: Content is not in JSON format')
        sys.exit(1)

else: # Note: You’ll want to use the text attribute to get the HTML.
    print ("~Content-type is specified as HTML format") 
    # print (resp.text)
    content = resp.text
    
 
# TODO: Make it work with this method later
# try:
#     resp = requests.get(url)
# except ConnectionError:
#     print (f"ERROR: invalid address specified {resp}")
#     sys.exit(1)
# except requests.exceptions.HTTPError as err:
#     print (f"ERROR: site responded with {err}")
#     sys.exit(1)
# else:
#     print (f"Site responded with code {resp.status_code}")
#     # print(resp)

# Writes the contents of the page out to the destination.
print (f"~Contents will be written to file named: {filename}")
print (f'~File will be encoded as: {resp.encoding}')

# Iterate using iter_lines
with open(filename, mode='w') as f:
    line_count = 0
    for line in resp.iter_lines():
        if line:
            line_count += 1
            if resp.encoding:
                line = line.decode(f'{resp.encoding}')
            f.write(line)
    print (f'~ {line_count} lines were written to {filename}')

# WRITE TO A FILE using 'requests.iter_content' as chunks.
# Streaming  ust be turned on in requests initilization
# We need fetch the URL again
resp = requests.get(url, stream=True)
with open(f'{filename}_chunked', mode='wb') as f:
    chunk_count = 0
    for chunk in resp.iter_content(chunk_size=128):
        if chunk:  # filter out keep-alive new chunks
            chunk_count += 1
            f.write(chunk)
    print (f'~ {chunk_count} chunks of 128b were written to {filename}')

# Write to a file based in 'Response.text' 
# with open(filename, mode='w') as f:
#     print (f"Contents will be written to {filename}")
#     for line in file_output:
#         f.write(line + "\n")

# Exit script
print(f"> DONE: File {filename} written successfuly!!!")
sys.exit(0)