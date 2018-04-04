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

visits = {house: set() for house in houses}
qs = {house: [(house, [house])] for house in houses}
def bfs_paths(graph, start, goals):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        yield None
        neighs = graph[vertex]
        visits[start].add(vertex)
        for neigh in neighs:
            for house, visit in visits.items():
                if house != start and neigh in visit:
                    # a = results[house]
                    # b = results[start]
                    # c = len(a) + len(b)
                    printdebug('solution! - house', house, 'to', start)
                    yield path + [neigh]
            if neigh in goals:
                # results[start].append(neigh)
                yield path + [neigh]
            elif neigh not in visits[start]:
                # results[start].append(neigh)
                queue.append((neigh, path + [neigh]))
# house BFS generators
gens = [bfs_paths(graph, house, houses - set([house])) for house in houses]
result = None
while not result:
    for gen in gens:
        res = next(gen)
        if res:
            result = res
            break

print(len(result) - 1)
