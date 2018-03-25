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

def permutate(sock, i, pairs, perms = {}): # using python mutable default function arguments
    for n in range(26):
        shifted = shift(sock, n)
        if shifted in perms:
            match = perms[shifted]
            pairs[i] = pairs[match] = 1 # pair socks
            break # return because all permutations already in hashtable.
        else:
            perms[shifted] = i

# SCAN INPUT
n = int(input())
pairs = {}
for i in range(n):
    pairs[i] = 0
    permutate(input(), i, pairs)
for i, paired in pairs.items():
    print(paired)
    
