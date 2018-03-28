# Author: 		Jeroen Overschie
# S-number:		s2995697
# Date:			28-03-2018
# Challenge:	MANHATTAN

import os
import sys
import math
from collections import deque

# LOGGING
def printdebug(*s):
    if "TEST" in os.environ:
        print(*s)

# REDIRECT STDIN
if "TEST" in os.environ:
    old_stdin = sys.stdin
    sys.stdin = open('./MANHATTAN/1.in')

# SCAN INPUT
[n, m] = [int(x) for x in input().split()]  # rows, columns
matrix = []
# graph = {}          # for finding buildings efficiently
stones = set()      # stones, e.g. building pieces
for i in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

    for j, cell in enumerate(row):  # store stones, e.g. building pieces
        if cell == 1:               # its a stone
            stones.add((i, j))

def peek(i, j):
    return None if i < 0 or i > n - 1 or j < 0 or j > m - 1 else (i, j)

def neighbors(tile):
    i, j = tile
    return filter(None, [
        peek(i - 1, j - 1), peek(i - 1, j), peek(i - 1, j + 1),
        peek(i,     j - 1),                 peek(i,     j + 1),
        peek(i + 1, j - 1), peek(i + 1, j), peek(i + 1, j + 1)
    ])

def isStone(tile):
    i, j = tile
    return True if matrix[i][j] == 1 else False

def construct(root): # recursively construct a building from 1 stone
    building = set([root])
    q = deque([root])
    while q:
        stone = q.pop()
        neighs = neighbors(stone)
        for neigh in neighs:
            if neigh not in building and isStone(neigh):
                building.add(neigh)
                q.append(neigh)
                # if neigh in stones:
                #     stones.remove(neigh)
    return building

buildings = []
while stones:
    stone = stones.pop()
    printdebug('STONE ', stone)

    # construct a new building
    building = construct(stone)
    printdebug('building', building)
    stones -= building # remove this building from building stones
    buildings.append(building)

print(-1)
