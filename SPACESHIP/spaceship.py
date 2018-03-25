# Author: 		Jeroen Overschie
# S-number:		s2995697
# Date:			21-03-2018
# Challenge:	SPACESHIP

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
    sys.stdin = open('./SPACESHIP/3.in')

# SCAN INPUT
[n, k] = [int(x) for x in input().split()]
spaceship = {}
for _ in range(n - 1):  # scan weighted edges
    [a, b, c] = [int(x) for x in input().split()]
    spaceship.setdefault(a, {})
    spaceship.setdefault(b, {})
    spaceship[a][b] = bool(c)
    # spaceship[b][a] = bool(c)

""" @returns whether last gate should be closed """
def dfs(graph, k, node, visited, result, savable = None):
    if node not in visited:
        # HANDLE PRESSURE
        total = result['pressure'] + result['potential']
        if savable and total > k:
            print('need to close before', node)
            return savable
        if result['pressure'] > k:          # explosion
            print('explosion')
            result['gates closed'] = -1
            return
        # spaceship not exploded yet, explore further
        visited.add(node)
        for neighbor, closable in graph[node].items():
            # HANDLE GATES
            print('from', node, 'to', neighbor, ', closable:', closable)
            if closable and savable:
                # new gate closing opportunity - ignore because we could close earlier
                pass
            if closable and not savable: # new gate opportunity
                print('gate opportunity at', (node, neighbor))
                savable = (node, neighbor)
            if savable:
                result['potential'] += 1
            else:
                result['pressure'] += 1

            # return whether we have to close this gate!!!!!!!!!!!!
            should_close = dfs(graph, k, neighbor, visited, result, savable)
            if closable and should_close:
                print('closing should_close', should_close)


def bfs(root, k):
    queue = deque(root) # enqueue all children of 1
    while queue:
        node = queue.popleft()
        printdebug(node)
        queue.extend(spaceship[node])
    return -1



# block 1 is depressurised first
gates = bfs(spaceship[1], k)
print(gates)
