# Author: 		Jeroen Overschie
# S-number:		s2995697
# Date:			25-03-2018
# Challenge:	SOCKS

import os
import sys
import math
import string

# LOGGING
def printdebug(*s):
    if "TEST" in os.environ:
        print(*s)

# REDIRECT STDIN
if "TEST" in os.environ:
    old_stdin = sys.stdin
    sys.stdin = open('./SOCKS/2.in')

def shift(text, n):
    s = ""
    for letter in text:
        index = ord(letter) - ord('a') + n
        s += string.ascii_lowercase[index % len(string.ascii_lowercase)]
    return s

def pair(sock, socks = set()): # using python mutable default function arguments
    for a in range(26):
        if shift(sock, a) in socks:
            return True
        else:
            socks.add(sock)
    return False

# SCAN INPUT
n = int(input())
for _ in range(n):
    sock = input()
    printdebug('SOCK', sock)
    paired = pair(sock)
    print(1 if paired else 0)

