#!/usr/bin/env python3.6

import argparse

parser = argparse.ArgumentParser(description='Search for words including partial word')
parser.add_argument('snippet', help='partial (or complete) string to search for in words file')

args = parser.parse_args()
snippet = args.snippet.lower()

with open('/usr/share/dict/words') as f:
    words = f.readlines()

# matches = []
# 
# for word in words:
#     if snippet in word.lower():
#         matches.append(word)

# the follwong line has exactsame meaning as the for loop above, 
# but uses 'list comprehention' to achive the same result
print([word.strip() for word in words if snippet in word.lower()])