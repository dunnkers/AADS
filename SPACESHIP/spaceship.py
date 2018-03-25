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

# travel through the spaceship, trying to save it
def travel(tree, root, k):
    blocks = deque([(root, 0, None)]) # enqueue all children of 1
    p = 1 # pressure
    g = 0 # closed gates
    while blocks:
        node, pp, gate = blocks.popleft() # pp = potential pressure
        printdebug('NODE', node, '(p =', p, ', pp =', pp, ',', gate, ')')
        for neighbor, closable in tree[node].items():
            printdebug('  →', node, '-', neighbor, '☑️' if closable else '')
            printdebug('\tp =', p, 'pp =', pp)
            ppnext = pp
            # first explores all blocks behind gates.
            if closable:
                ppnext += 1
                blocks.append((neighbor, ppnext, (node, neighbor)))
            elif gate:  # in a gate segment
                if p + pp + 1 > k:  # we cannot lose this block. close a gate!
                    printdebug('closing ', gate)
                    g += 1
                    break
                else:
                    printdebug('in gate segment, no pressure buildup')
                    pp += 1
                    blocks.appendleft((neighbor, ppnext, gate))
            else:
                printdebug('\t💠 [', neighbor, '] lost')
                p += 1
                blocks.appendleft((neighbor, ppnext, gate))
    return g

# notes
# we could use node->next like strategy instead of dict. but o(1) lookup so ok.


# block 1 is depressurised first
gates = travel(spaceship, 1, k)
print(gates)
