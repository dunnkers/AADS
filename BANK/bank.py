# Author: 		Jeroen Overschie
# S-number:		s2995697
# Date:			20-03-2018
# Challenge:	BANK

import os
import sys
import math
import queue

# REDIRECT STDIN
if "TEST" in os.environ:
    old_stdin = sys.stdin
    sys.stdin = open('./BANK/2.in')


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

queue = queue.Queue()
queue.put(start)


# def bfs_paths(graph, start, goal):
#     queue = [(start, [start])]
#     while queue:
#         (vertex, path) = queue.pop(0)
#         for next in graph[vertex] - set(path):
#             if next == goal:
#                 yield path + [next]
#             else:
#                 queue.append((next, path + [next]))


# paths = list(bfs_paths(graph, start, end))
# print(paths)


visited = set()
while not queue.empty():
    vertex = queue.get()
    if vertex not in visited:
        print('visiting', vertex)
        visited.add(vertex)
        neighbors = graph[vertex].items()
        for neighbor in neighbors:
            (node, dist) = neighbor
            if node not in visited:
                queue.put(node)
    pass


print(-1)

from collections import defaultdict
from heapq import heappop, heappush


def dijkstra(graph, src, dest, visited=[], distances={}, predecessors={}):
    """ calculates a shortest path tree routed in src
    """
    # a few sanity checks
    if src not in graph:
        raise TypeError('The root of the shortest path tree cannot be found')
    if dest not in graph:
        raise TypeError('The target of the shortest path cannot be found')
    # ending condition
    if src == dest:
        # We build the shortest path and display it
        path = []
        pred = dest
        while pred != None:
            path.append(pred)
            pred = predecessors.get(pred, None)
        print('shortest path: '+str(path)+" cost="+str(distances[dest]))
    else:
        # if it is the initial  run, initializes the cost
        if not visited:
            distances[src] = 0
        # visit the neighbors
        for neighbor in graph[src]:
            if neighbor not in visited:
                new_distance = distances[src] + graph[src][neighbor]
                if new_distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = src
        # mark as visited
        visited.append(src)
        # now that all neighbors have been visited: recurse
        # select the non visited node with lowest distance 'x'
        # run Dijskstra with src='x'
        unvisited = {}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k, float('inf'))
        x = min(unvisited, key=unvisited.get)
        dijkstra(graph, x, dest, visited, distances, predecessors)


# graph = {'s': {'a': 2, 'b': 1},
#         'a': {'s': 3, 'b': 4, 'c': 8},
#         'b': {'s': 4, 'a': 2, 'd': 2},
#         'c': {'a': 2, 'd': 7, 't': 4},
#         'd': {'b': 1, 'c': 11, 't': 5},
#         't': {'c': 3, 'd': 5}}
dijkstra(graph, start, end)
