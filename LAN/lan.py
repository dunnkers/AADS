# Author: 		Jeroen Overschie
# S-number:		s2995697
# Date:			21-03-2018
# Challenge:	SPACESHIP

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
    sys.stdin = open('./LAN/2.in')

# SCAN INPUT
n = int(input())
s = [int(x) for x in input().split()]
tree = {}
x = None
for _ in range(n - 1):  # scan weighted edges
    [a, b] = [int(x) for x in input().split()]
    tree.setdefault(a, set())
    tree.setdefault(b, set())
    tree[a].add(b)
    tree[b].add(a)
    if x == None:
        x = a

def points(n):
    return s.copy()[:(n + 1)]

def point(n):
    return s[n]

visited = set()
q = deque([ x ])
while q:
    node = q.pop()
    visited.add(node)

    adjs = tree[node]
    amt = len(adjs)
    pt = point(amt)
    pts = points(amt)
    printdebug('points for', node,':',pts, 'current=',pt)
    maxit = max(pts)
    if maxit > pt:
        printdebug('optimizing', node)
        for adj in adjs:  # 2nd tree[node] call
            printdebug('points for', adj, ':', points(len(tree[adj])))
            # if adj not in visited:
            #     q.append(adj)

