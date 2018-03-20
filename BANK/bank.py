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
# def do_dijkstra(graph, src, dests):
#     return dijkstra(graph, src, 
#                     dests if isinstance(dests, list) else [dests], {}, {}, [], [])


# def dijkstra(graph, node, dests, dists, prev, visited, results):
#     if node not in graph:
#         return None

#     if node in dests: # we reached one of the destinations
#         path = []
#         pred = node
#         while pred != None:
#             path.append(pred)
#             pred = prev.get(pred, None)
#         printdebug('found a path: '+str(path)+" cost="+str(dists[node]))
#         results.append((node, dists[node]))
#         dests.remove(node)
#         yield (node, dists[node])
#     if len(dests) == 0:  # we computed paths to all destinations
#         # yield results
#         return None
#     else:
#         if not visited: # visited is empty
#             dists[node] = 0
#         # visit the neighbors
#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 newDist = dists[node] + graph[node][neighbor]
#                 if newDist < dists.get(neighbor, float('inf')): # infinity
#                     dists[neighbor] = newDist
#                     prev[neighbor] = node
        
#         visited.append(node) # we visited

#         unvisited = {}
#         for k in graph:
#             if k not in visited:
#                 unvisited[k] = dists.get(k, float('inf')) # compare to infinity
                
#         newNode = min(unvisited, key=unvisited.get)
#         yield from dijkstra(graph, newNode, dests, dists, prev, visited, results)

# def rob_bank(graph, start, end, banks):
#     bank_paths = do_dijkstra(graph, end, banks.copy())
#     if not bank_paths:
#         return -1
#     printdebug('computed paths from end to bank(s).')
#     for (bank_node, endcost) in bank_paths:
#         printdebug('testing bank', bank_node, 'endcost', endcost)
#         if endcost >= p:
#             return -1
#         start_to_bank = next(do_dijkstra(graph, bank_node, [start])) # first
#         if start_to_bank: # bank is reachable from start
#             (start_node, startcost) = start_to_bank
#             printdebug('found a path from bank to start', start_node, 'cost', startcost)
#             return startcost + endcost
#     return -1

# print(rob_bank(graph, start, end, banks))


# def Dijkstra(graph, n, start): # `n` vertices
#     A = [None] * (n + 1) # using an array here is faster than dict..
#     queue = [(0, start)]
#     while queue:
#         path_len, v = heappop(queue)
#         if A[v] is None:  # v is unvisited
#             A[v] = path_len
#             for w, edge_len in graph[v].items(): # neighbors
#                 if A[w] is None: # not visited yet
#                     heappush(queue, (path_len + edge_len, w))

#     return [0 if x is None else x for x in A]


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
# can be a list comprehension too,..
for (bank, cost) in DijkstraSearch(graph, n, start, banks):
    reachability[bank] = cost
# printdebug('reachability =', reachability)

# start_paths = Dijkstra(graph, n, start)
# printdebug(start_paths)

for (bank, cost) in DijkstraSearch(graph, n, end, banks):
    if reachability[bank]:
        printdebug('robbing bank', bank)
        print(cost + reachability[bank])
        exit()
print(-1)


# for path in Dijkstra(graph, n, start):
#     print('path from start to vertex', _, 'costs', path)
