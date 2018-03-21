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
    sys.stdin = open('./BANK/3.in')

# SCAN INPUT
[n, m, o, p] = [int(x) for x in input().split()]
banks = set(int(x) for x in input().split()) # of length `o`
graph = {}
for _ in range(m): # scan weighted edges
    [a, b, c] = [int(x) for x in input().split()]
    graph.setdefault(a, {})
    graph.setdefault(b, {})
    graph[a][b] = c
    graph[b][a] = c
[start, end] = [int(x) for x in input().split()]


# DIJKSTRA
def dijkstra(graph, n, start, banks, p, targets):  # `n` vertices
    queue = [(0, start, False)]  # init queue
    L = [None] * (n + 1)  # path lengths. using an array here is faster than dict.
    while queue:
        path_len, node, tobank = heappop(queue)
        if L[node] is None and node in graph:  # node is unvisited
            if node in banks and path_len < p:
                tobank = path_len
            if node in targets:
                yield (node, path_len, tobank)
            L[node] = path_len
            for w, edge_len in graph[node].items():  # neighbors
                if L[w] is None:  # not visited yet
                    heappush(queue, (path_len + edge_len, w, tobank))


# PRE-COMPUTE ALL PATHS FROM START -> BANKS
# rob = {bank: cost for (bank, cost) in dijkstra(graph, n, start, banks)}

# we only compute bank distances for banks we can reach from start
# hide = {bank: cost for (bank, cost) in dijkstra(graph, n, end, rob.keys(), rob)}

robberies = {} # possible robberies
for (bank, cost, tobank) in dijkstra(graph, n, end, banks, p, [start]):
    if tobank == False:
        continue
    if tobank != False and tobank < p:
        printdebug('(possibly) robbing bank', bank, tobank, cost)
        robberies[bank] = cost
    else:
        break
if robberies:
    best_to_rob = 1000000
    for (bank, cost) in dijkstra(graph, n, start, banks, p, robberies.keys()):
        curr = cost + robberies[bank]
        if curr < best_to_rob:
            best_to_rob = curr
    print(best_to_rob)
else:
    print(-1)
