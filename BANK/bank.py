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
def do_dijkstra(graph, src, dests):
    return dijkstra(graph, src, 
                    dests if isinstance(dests, list) else [dests], {}, {}, [], [])


def dijkstra(graph, node, dests, dists, prev, visited, results):
    if node not in graph:
        return None

    if node in dests: # we reached one of the destinations
        path = []
        pred = node
        while pred != None:
            path.append(pred)
            pred = prev.get(pred, None)
        # printdebug('found a path: '+str(path)+" cost="+str(dists[node]))
        results.append((node, dists[node]))
        dests.remove(node)

    if len(dests) == 0:  # we computed paths to all destinations
        return results
    else:
        if not visited: # visited is empty
            dists[node] = 0
        # visit the neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                newDist = dists[node] + graph[node][neighbor]
                if newDist < dists.get(neighbor, float('inf')): # infinity
                    dists[neighbor] = newDist
                    prev[neighbor] = node
        
        visited.append(node) # we visited

        unvisited = {}
        for k in graph:
            if k not in visited:
                unvisited[k] = dists.get(k, float('inf')) # compare to infinity
                
        newNode = min(unvisited, key=unvisited.get)
        return dijkstra(graph, newNode, dests, dists, prev, visited, results)


def rob_bank(graph, start, end, banks):
    bank_paths = do_dijkstra(graph, end, banks.copy())
    if not bank_paths:
        return -1
    printdebug('computed paths from end to bank(s).')
    for (bank_node, endcost) in bank_paths:
        printdebug('testing bank', bank_node, 'endcost', endcost)
        if endcost >= p:
            return -1
        start_to_bank = do_dijkstra(graph, bank_node, [start])[0]
        if start_to_bank: # bank is reachable from start
            (start_node, startcost) = start_to_bank
            printdebug('found a path from bank to start', start_node, 'cost', startcost)
            return startcost + endcost
    print('-1')

print(rob_bank(graph, start, end, banks))
