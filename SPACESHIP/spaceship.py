# Author: 		Jeroen Overschie
# S-number:		s2995697
# Date:			21-03-2018
# Challenge:	SPACESHIP

import os
import sys
import math

# LOGGING
def printdebug(*s):
    if "TEST" in os.environ:
        print(*s)


# REDIRECT STDIN
if "TEST" in os.environ:
    old_stdin = sys.stdin
    sys.stdin = open('./SPACESHIP/2.in')

# SCAN INPUT
[n, k] = [int(x) for x in input().split()]
spaceship = {}
for _ in range(n - 1):  # scan weighted edges
    [a, b, c] = [int(x) for x in input().split()]
    spaceship.setdefault(a, {})
    spaceship.setdefault(b, {})
    spaceship[a][b] = bool(c)
    spaceship[b][a] = bool(c)


# DFS
def travel(spaceship, start): # DFS implementation
    # stack = [ start ]
    # visited = set()
    # while stack:
    #     block = stack.pop()
    #     if block not in visited:
    #         stack.extend(spaceship[block] - visited)
    #         visited.add(block)
    #         printdebug('visited', block)
    pass


travel(spaceship, spaceship[1]) # block 1 is de-pressurised

print(-1)
