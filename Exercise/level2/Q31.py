'''Given a block of text with several email addresses mixed in, use regex to find and print all
valid email addresses.'''

import re

exp = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

txt = list(input("Enter yoyur text : ").split())

for l in txt:
    if re.fullmatch(exp,l):
        print(l)

