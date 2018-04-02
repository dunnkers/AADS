# Author: 		Jeroen Overschie
# S-number:		s2995697
# Date:			30-03-2018
# Challenge:	FRIENDS

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
    sys.stdin = open('./FRIENDS/2.in')

# SCAN INPUT
[n, m, k] = [int(x) for x in input().split()]
graph = {}
for _ in range(m):
    [a, b] = [int(x) for x in input().split()]
    graph.setdefault(a, set())
    graph.setdefault(b, set())
    graph[a].add(b)
    graph[b].add(a)
houses = set(int(x) for x in input().split())

def bfs_paths(graph, start, goals):
    queue = [(start, [start])]
    visited = set()
    while queue:
        (vertex, path) = queue.pop(0)
        yield None
        neighs = graph[vertex]
        visited.add(vertex)
        for neigh in neighs:
            if neigh in goals:
                yield path + [neigh]
            elif neigh not in visited:
                queue.append((neigh, path + [neigh]))

# house BFS generators
gens = [bfs_paths(graph, house, houses - set([house])) for house in houses]
result = None
while not result:
    for gen in gens:
        res = next(gen)
        if res:
            result = res

print(len(result) - 1)
