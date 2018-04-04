# Author: 		Jeroen Overschie
# S-number:		s2995697
# Date:			28-03-2018
# Challenge:	MANHATTAN

import os
import sys
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
    spotrect = Building(spot[1], spot[0], 1, 1)
    return building.distance(spotrect)

def findWidth(gen, i, spots):
    width = 1
    for j, cell in gen:  # tuple (j, cell)
        if cell == 0:
            spots.add((i, j))
            break
        else:
            width += 1
    return width

class Building:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def distance(self, spot):
        xdiff = abs(self.x - spot.x)
        wsum = (self.width + spot.width)
        if xdiff <= wsum:
            dx = 0
        else:
            dx = xdiff - wsum
        ydiff = abs(self.y - spot.y)
        hsum = (self.height + spot.height)
        if ydiff <= hsum:
            dy = 0
        else:
            dy = ydiff - hsum

        # dx = abs(self.x - spot.x) - (self.width + spot.width)
        # dy = abs(self.y - spot.y) - (self.height + spot.height)
        return dx + dy
    
    def xDistance(self, spotx):
        east = (self.x + self.width - 1) # east point # width is at least 1
        if spotx >= self.x and spotx <= east: # between
            return 0
        elif spotx > east: # this stuff can also be done with a abs()?
            return spotx - east
        else: # spotx < self.x
            return self.x - spotx

    def yDistance(self, spoty):
        south = (self.y + self.height - 1) # height is at least 1
        if spoty >= self.y and spoty <= south: # between
            return 0
        elif spoty > south:
            return spoty - south
        else: # spoty < self.y
            return self.y - spoty
    
    def __str__(self):
        return "[Building (x = %d, y = %d) %dx%d]" % (self.x, self.y, self.width, self.height)

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
printdebug('matrix  construction:', time.time() - s, 'sec')

# COMPUTE BUILDINGS
def computeBuildings(stones):
    buildings = []
    while stones:
        stone = stones.pop()
        # _, j = stone
        # printdebug('STONE ', stone)

        # construct a new building
        building = constructFrom(stone, verticalNeighbors) # left-vertical segment
        stones -= building          # remove this building from building stones
        width = corners[stone]      # arbitrary stone; its a corner
        y, x = min(building)     # top tile
        bottom, _ = max(building)  # bottom tile
        height = bottom - y + 1

        buildings.append(Building(x, y, width, height))
        # printdebug('BUILDING x, y = (', x, ',', y, '), width=', width, 'height=', height)
        # printdebug('BUILDING', building)
    return buildings
s = time.time()
buildings = computeBuildings(stones)
printdebug('building contruction:', time.time() - s, 'sec')

# COMPUTE DISTANCES
def computeTotalXDist(spot, buildings, bestdist):
    _, spotx = spot
    total = 0
    for building in buildings:
        xdist = building.xDistance(spotx)
        total += xdist
        if total > bestdist:  # break early when we already exceeded dist
            break
    return total

def computeTotalYDist(spot, buildings, bestdist):
    spoty, _ = spot
    total = 0
    for building in buildings:
        ydist = building.yDistance(spoty)
        total += ydist
        if total > bestdist:  # break early when we already exceeded dist
            break
    return total

def computeBestDistances(spots, buildings, computeTotalDist):
    distances = {}
    bestdist = 1000000
    while spots:
        spot = spots.pop()
        total = computeTotalDist(spot, buildings, bestdist)
        if total < bestdist:
            bestdist = total
        # PERF use a >heapq< or bisect
        distances.setdefault(total, [])
        distances[total].append(spot)

        # printdebug('\tTOT DIST:', total)
    return distances

s = time.time()
distances = computeBestDistances(spots, buildings, computeTotalXDist)
printdebug('x distance computation:', time.time() - s, 'sec')

# GET SMALLEST X DIST
s = time.time()
least = min(distances.keys())
dists = distances[least]
printdebug('smallest   x distance:', time.time() - s, 'sec')

# COMPUTE Y DIST
s = time.time()
distancesWithY = computeBestDistances(dists, buildings, computeTotalYDist)
printdebug('y distance computation:', time.time() - s, 'sec')


# COMPUTE SMALLEST DISTANCE
s = time.time()
def getSmallest(distances):
    least = min(distances.keys())
    dists = distances[least]
    # sorts tuples by (x, y) first by x than y. which is row then column.
    return sorted(dists)[0]
x, y = getSmallest(distancesWithY)
printdebug('smallest   y distance:', time.time() - s, 'sec')
print(x + 1, y + 1) # convert to 1-indexed sytem
