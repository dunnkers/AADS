# Author: 		Jeroen Overschie
# S-number:		s2995697
# Date:			28-03-2018
# Challenge:	MANHATTAN

import os
import sys
import math
from collections import deque
from heapq import heappush, heappop

# LOGGING
def printdebug(*s):
    if "TEST" in os.environ:
        print(*s)

# REDIRECT STDIN
if "TEST" in os.environ:
    old_stdin = sys.stdin
    sys.stdin = open('./MANHATTAN/2.in')

# SCAN INPUT
[n, m] = [int(x) for x in input().split()]  # rows, columns
matrix = []
stones = set()          # stones, e.g. building pieces
spots = set()           # empty spots e.g. potential ice-cream places
# -> CONSTRUCT MATRIX AND STONES & SPOTS SETS
for i in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

    for j, cell in enumerate(row):  # store stones, e.g. building pieces
        if cell == 1:               # its a stone
            stones.add((i, j))
        else:                       # its a spot
            spots.add((i, j))

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
        for neigh in neighbors(q.pop()):
            if neigh not in building and isStone(neigh):
                building.add(neigh)
                q.append(neigh)
    return building

# COMPUTE BUILDINGS
buildings = []
while stones:
    stone = stones.pop()
    printdebug('STONE ', stone)

    # construct a new building
    building = construct(stone)
    printdebug('BUILDING', building)
    stones -= building          # remove this building from building stones
    buildings.append(building)

def distance(spot, stone):
    return abs(spot[0] - stone[0]) + abs(spot[1] - stone[1])

def distanceTo(spot, building):
    return min(map(lambda stone: distance(spot, stone), building))

# COMPUTE DISTANCES
distances = {}
while spots:
    spot = spots.pop()
    printdebug('SPOT', spot)
    total = sum(map(lambda building: distanceTo(spot, building), buildings))

    distances.setdefault(total, [])
    distances[total].append(spot)

    printdebug('TOT DIST:', total)

# COMPUTE SMALLEST DISTANCE
least = min(distances.keys())
dists = distances[least]
# sorts tuples by (x, y) first by x than y. which is row then column.
x, y = sorted(dists)[0]
print(x + 1, y + 1) # convert to 1-indexed sytem
