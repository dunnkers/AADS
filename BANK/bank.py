# Author: 		Jeroen Overschie
# S-number:		s2995697
# Date:			20-03-2018
# Challenge:	BANK

import os
import sys
import math
import queue

# LOGGING
def printdebug(*s):
    if "TEST" in os.environ:
        print(*s)

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

def dodijkstra(graph, src, dests):
    return dijkstra(graph, src, 
    dests if isinstance(dests, list) else [dests], [], {}, {}, [])

def dijkstra(graph, src, dests, visited, distances, predecessors, results):
    """ calculates a shortest path tree routed in src
    """
    # a few sanity checks
    if src not in graph:
        return None
    if src in dests:
        # We build the shortest path and display it
        path = []
        pred = src
        while pred != None:
            path.append(pred)
            pred = predecessors.get(pred, None)
        printdebug('a shortest path: '+str(path)+" cost="+str(distances[src]))
        results.append((src, distances[src]))
        dests.remove(src)
    # ending condition
    if len(dests) == 0:
        return results
    else:
        # if it is the initial run, initializes the cost
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
        return dijkstra(graph, x, dests, visited, distances, predecessors, results)


# graph = {'s': {'a': 2, 'b': 1},
#         'a': {'s': 3, 'b': 4, 'c': 8},
#         'b': {'s': 4, 'a': 2, 'd': 2},
#         'c': {'a': 2, 'd': 7, 't': 4},
#         'd': {'b': 1, 'c': 11, 't': 5},
#         't': {'c': 3, 'd': 5}}
bank_paths = dodijkstra(graph, end, banks.copy())
if not bank_paths:
    print('-1')
    exit()
printdebug('computed paths from end to bank(s).')
for (bank_node, endcost) in bank_paths:
    printdebug('testing bank', bank_node, 'endcost', endcost)
    if endcost >= p:
        print('-1')
        break
    start_to_bank = dodijkstra(graph, bank_node, [start])[0]
    if not start_to_bank:
        break
    else:
        (start_node, startcost) = start_to_bank
        printdebug('found a path from bank to start', start_node, 'cost', startcost)
        print(startcost + endcost)
        exit(0)
print('-1')
