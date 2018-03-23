# Author: 		Jeroen Overschie
# S-number:		s2995697
# Date:			21-03-2018
# Challenge:	SPACESHIP

import os
import sys
import math

# LOGGING
def printdebug(*s):
    if "TEST" in os.environ:
        print(*s)


# REDIRECT STDIN
if "TEST" in os.environ:
    old_stdin = sys.stdin
    sys.stdin = open('./SPACESHIP/2.in')

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
def dfs(graph, k, node, visited, result, savable = False):
    if node not in visited:
        total = result['pressure'] + result['potential']
        if savable and total > k:
            print('need to close before', node)
            return True
        if result['pressure'] > k:          # will spaceship explode?
            result['gates closed'] = -1
            return
        # spaceship not exploded yet, explore further
        visited.add(node)
        for neighbor, closable in graph[node].items():
            print('from', node, 'to', neighbor, ', closable:', closable)
            if closable:
                savable = True
            if savable:
                result['potential'] += 1
            else:
                result['pressure'] += 1

            # return whether we have to close this gate!!!!!!!!!!!!
            should_close = dfs(graph, k, neighbor, visited, result, savable)
            if closable and should_close:
                print('closing', node, '-', neighbor)


# block 1 is depressurised
result = {
    'pressure': 1,
    'potential': 0,
    'gates closed': 0
}
dfs(spaceship, k, 1, set(), result)
printdebug(result)
print(result['gates closed'])
