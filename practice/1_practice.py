'''Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language
Coding:
if the word contains atleast 3 characters, remove the first letter and append it at the end now append three random characters at the starting 
else: simply reverse the string

Decoding:
if the word contains less than 3 characters, reverse it else: remove 3 random characters from start . Now remove the last letter and append it to the 
beginning

Your program should ask whether you want to code or decode'''

import random
import string

def encode(s):
    if len(s) >= 3:
        ch = s[0]
        s = s[1:]
        s += ch
        r = ''.join(random.choices(string.ascii_letters,k=3))
        r += s
        return r
    else:
        return s[::-1]

print(encode("tarun"))

def decode(s):
    if 3>len(s):
        return s[::-1]
    else:
        s = s[3:]
        f = s[-1]
        s = s[:-1]
        return f + s

print(decode("peXarunt"))