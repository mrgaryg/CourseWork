#!/usr/bin/env python

import os
import sys
import requests
import json

url = os.getenv('url', default = 'http://google.com')
filename = 'iter_test.out'

r = requests.get(url, stream=True)

print (f'request url is {r.url}')
print (f'request encoding is: {r.encoding}')
# print (f'r.content is: {r.content}')

with open(filename, mode='w') as f:
    print (f'> writing to: {filename}')
    line_count = 0
    for line in r.iter_lines():
        if line:
            line_count += 1
            if r.encoding:
                line = line.decode(f'{r.encoding}')
            f.write(f"line {line_count}: {line} \n")

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



# DO YOU WANT THE SCRIPT TO READ BACK THE WRITTEN FILE
# with open(filename, mode='r') as fr:
#     print (f'reading from {fr}')
#     for line in fr.readlines():
#         print (line)

print(f'>Done!!! {line_count} lines written to {filename}')
sys.exit(0)