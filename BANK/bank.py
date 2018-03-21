# Author: 		Jeroen Overschie
# S-number:		s2995697
# Date:			20-03-2018
# Challenge:	BANK

import os
import sys
import math
from heapq import heappush, heappop
from collections import Counter

# LOGGING
def printdebug(*s):
    if "TEST" in os.environ:
        print(*s)

# REDIRECT STDIN
if "TEST" in os.environ:
    old_stdin = sys.stdin
    sys.stdin = open('./BANK/start_bank_dist.in')

# SCAN INPUT
[n, m, o, p] = [int(x) for x in input().split()]
banks = [int(x) for x in input().split()] # of length `o`
graph = {}
for _ in range(m): # scan weighted edges
    [a, b, c] = [int(x) for x in input().split()]
    graph.setdefault(a, {})
    graph.setdefault(b, {})
    graph[a][b] = c
    graph[b][a] = c
    pass
[start, end] = [int(x) for x in input().split()]


# DIJKSTRA
def dijkstra(graph, n, start, targets):  # `n` vertices
    queue = [(0, start)] # init queue
    L = [None] * (n + 1) # path lengths. using an array here is faster than dict.
    while queue:
        path_len, node = heappop(queue)
        if L[node] is None and node in graph:  # node is unvisited
            if node in targets:
                yield (node, path_len)
            L[node] = path_len
            for w, edge_len in graph[node].items():  # neighbors
                if L[w] is None:  # not visited yet
                    heappush(queue, (path_len + edge_len, w))


# PRE-COMPUTE ALL PATHS FROM START -> BANKS
# rob = {bank: cost for (bank, cost) in dijkstra(graph, n, start, banks)}

# we only compute bank distances for banks we can reach from start
# hide = {bank: cost for (bank, cost) in dijkstra(graph, n, end, rob.keys(), rob)}

robberies = {} # possible robberies
for (bank, cost) in dijkstra(graph, n, end, banks):
    if cost < p:
        printdebug('(possibly) robbing bank', bank)
        robberies[bank] = cost
    else:
        break
if robberies:
    to_rob = []
    for (bank, cost) in dijkstra(graph, n, start, robberies.keys()):
        heappush(to_rob, (cost + robberies[bank], bank))
        
    cost, rob = heappop(to_rob)
    print(cost)
else:
    print(-1)
