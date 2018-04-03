# Author: 		Jeroen Overschie
# S-number:		s2995697
# Date:			28-03-2018
# Challenge:	MANHATTAN

import os
import sys
import math
from collections import deque
from heapq import heappush, heappop

# Profiling. Also done using `python3 -m cProfile manhattan.py < 1_themis.in`
import time

# LOGGING
def printdebug(*s):
    if "TEST" in os.environ:
        print(*s)

# REDIRECT STDIN
if "TEST" in os.environ:
    old_stdin = sys.stdin
    sys.stdin = open('./MANHATTAN/1_themis.in')

def peek(i, j):
    return None if i < 0 or i > n - 1 or j < 0 or j > m - 1 else (i, j)

def verticalNeighbors(tile):
    i, j = tile
    return filter(None, [peek(i - 1, j), peek(i + 1, j), ])

def isStone(tile):
    i, j = tile
    return True if matrix[i][j] == 1 else False

def constructFrom(root, func):  # recursively construct a building from 1 stone
    building = set([root])
    q = deque([root])
    while q:
        for neigh in func(q.pop()):
            if neigh not in building and isStone(neigh):
                building.add(neigh)
                q.append(neigh)
    return building

def distance(spot, stone):
    return abs(spot[0] - stone[0]) + abs(spot[1] - stone[1])


def distanceTo(spot, building):
    return min(map(lambda stone: distance(spot, stone), building))

def findWidth(gen, i, spots):
    width = 0
    for j, cell in gen:  # tuple (j, cell)
        if cell == 0:
            spots.add((i, j))
            break
        else:
            width += 1
    return width

# SCAN INPUT
s = time.time()
[n, m] = [int(x) for x in input().split()]  # rows, columns
matrix = []
stones = set()          # stones, e.g. building pieces
spots = set()           # empty spots e.g. potential ice-cream places
construction = {}
corners = {}
buildings = []
# -> CONSTRUCT MATRIX AND STONES & SPOTS SETS
for i in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)
    # maybe use a zip here..
    gen = enumerate(row)
    for j, cell in gen:  # store stones, e.g. building pieces
        tile = (i, j)
        if cell == 1:               # its a stone
            stones.add(tile)
            corners[tile] = findWidth(gen, i, spots)
        else:                       # its a spot
            spots.add(tile)
printdebug('matrix construction:', time.time() - s, 'sec')

# COMPUTE BUILDINGS
s = time.time()
buildings = []
while stones:
    stone = stones.pop()
    _, j = stone
    # printdebug('STONE ', stone)

    # construct a new building
    building = constructFrom(stone, verticalNeighbors) # left-vertical segment
    stones -= building          # remove this building from building stones
    width = corners[stone]
    top, _ = min(building)     # top tile
    bottom, _ = max(building)  # bottom tile
    # right-vertical segment
    building |= set([(i, j + width) for i, j in building])
    # top segment
    building |= set([(top, col) for col in range(j + 1, j + width)])
    # bottom segment
    building |= set([(bottom, col) for col in range(j + 1, j + width)])

    buildings.append(building)
    # printdebug('BUILDING', building)
printdebug('building contruction:', time.time() - s, 'sec')

# COMPUTE DISTANCES
s = time.time()
distances = {}
while spots:
    spot = spots.pop()
    # printdebug('SPOT', spot)
    total = sum(map(lambda building: distanceTo(spot, building), buildings))

    distances.setdefault(total, [])
    distances[total].append(spot)

    # printdebug('TOT DIST:', total)
printdebug('distance computation:', time.time() - s, 'sec')

# COMPUTE SMALLEST DISTANCE
s = time.time()
least = min(distances.keys())
dists = distances[least]
# sorts tuples by (x, y) first by x than y. which is row then column.
x, y = sorted(dists)[0]
printdebug('smallest distance computation:', time.time() - s, 'sec')
print(x + 1, y + 1) # convert to 1-indexed sytem
