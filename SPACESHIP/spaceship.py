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
    spaceship[b][a] = bool(c)

# travel through the spaceship, trying to save it
def travel(tree, root, k, visited = set()):
    blocks = deque([(root, 0, None)]) # enqueue all children of 1
    p = 1 # pressure
    g = 0 # closed gates
    while blocks:
        node, pp, gate = blocks.popleft() # pp = potential pressure
        if node not in visited:
            visited.add(node)
            printdebug('NODE', node, '(p =', p, ', pp =', pp, ',', gate, ')')
            for neighbor, closable in tree[node].items():
                printdebug('  →', node, '-', neighbor, '☑️' if closable else '')
                printdebug('\tp =', p, 'pp =', pp)
                ppnext = pp
                # first explores all blocks behind gates.
                if gate:  # in a gate segment
                    if p + pp + 1 > k:  # we cannot lose this block. close a gate!
                        printdebug('closing ', gate)
                        g += 1
                        break
                    else:
                        printdebug('in gate segment, no pressure buildup')
                        pp += 1
                        blocks.appendleft((neighbor, ppnext, gate))
                elif closable:
                    ppnext += 1
                    blocks.append((neighbor, ppnext, (node, neighbor)))
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
