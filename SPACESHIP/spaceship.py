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

def visit(tree, node, callback, visited=set()):
    visited.add(node)
    for neighbor, arg in tree[node].items():
        if neighbor in visited:
            continue
        callback(neighbor, arg)


# travel through the spaceship, trying to save it
def travel(tree, root, k, visited = set(), depressurised = set()):
    blocks = deque([root]) # enqueue all children of 1
    gates = deque()  # heapq!!

    p = 1  # pressure
    def pressurised(node, closable):
        if closable:
            gates.append(node)
        else:
            printdebug(node, closable)
            p += 1
            blocks.appendleft(node)
    g = 0 # closed gates
    while blocks:
        node = blocks.popleft()


        visit(tree, node, pressurised)
        # visited.add(node)
        # printdebug('NODE', node, '(p =', p, ')')
        # for neighbor, closable in tree[node].items():
        #     if neighbor in visited:
        #         continue
        #     printdebug('  →', node, '-', neighbor, '☑️' if closable else '')
        #     if closable:
        #         # blocks.append((neighbor, pp, (node, neighbor)))
        #         pass
        #     elif neighbor not in depressurised:
        #         printdebug('\t💠 [', neighbor, '] lost')
        #         depressurised.add(neighbor)
        #         p += 1
        #         blocks.appendleft(neighbor)
    return g

# block 1 is depressurised first
gates = travel(spaceship, 1, k)
print(gates)
