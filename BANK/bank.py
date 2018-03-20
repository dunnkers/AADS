# Author: 		Jeroen Overschie
# S-number:		s2995697
# Date:			20-03-2018
# Challenge:	BANK

import os
import sys
import math
from heapq import heappush, heappop

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


# # DIJKSTRA
def Dijkstra(graph, n, start): # `n` vertices
    A = [None] * (n + 1) # using an array here is faster than dict..
    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        if A[v] is None:  # v is unvisited
            A[v] = path_len
            for w, edge_len in graph[v].items(): # neighbors
                if A[w] is None: # not visited yet
                    heappush(queue, (path_len + edge_len, w))

    return [0 if x is None else x for x in A]


def DijkstraSearch(graph, n, start, targets):  # `n` vertices
    queue = [(0, start)] # init queue
    L = [None] * (n + 1) # path lenghts. using an array here is faster than dict.
    while queue:
        path_len, node = heappop(queue)
        # printdebug('visiting', node)
        if L[node] is None and node in graph:  # node is unvisited
            if node in targets:
                # printdebug('reached the end!', path_len)
                yield (node, path_len)
            L[node] = path_len
            for w, edge_len in graph[node].items():  # neighbors
                if L[w] is None:  # not visited yet
                    heappush(queue, (path_len + edge_len, w))


# PRE-COMPUTE ALL PATHS FROM START -> BANKS
reachability = dict.fromkeys(banks, False)
# can be a list/dict comprehension too,..
for (bank, cost) in DijkstraSearch(graph, n, start, banks):
    reachability[bank] = cost
# printdebug('reachability =', reachability)

start_paths = Dijkstra(graph, n, start)
printdebug(start_paths)

for (bank, cost) in DijkstraSearch(graph, n, end, banks):
    if not cost >= p and reachability[bank]:
        printdebug('robbing bank', bank)
        print(cost + reachability[bank])
        exit()
print(-1)


# for path in Dijkstra(graph, n, start):
#     print('path from start to vertex', _, 'costs', path)
