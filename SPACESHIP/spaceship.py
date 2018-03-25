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
tree = {}
for _ in range(n - 1):  # scan weighted edges
    [a, b, c] = [int(x) for x in input().split()]
    tree.setdefault(a, {})
    tree.setdefault(b, {})
    tree[a][b] = bool(c)
    tree[b][a] = bool(c)

def visit(tree, node, callback, args, visited=set()):
    visited.add(node)
    for neighbor, arg in tree[node].items():
        if neighbor in visited:
            continue
        callback(neighbor, arg, args)

class Spaceship(object):
    def __init__(self, spaceship):
        self.spaceship = spaceship
        self.gates = deque()  # heapq!!
        self.gatemap = {}
        self.pressure = 1
        self.gates_closed = 0

    def pressurised(self, node, closable, q):
        if closable:
            self.gates.append(node)
        else:
            q.append(node)
            printdebug(node, closable)
            self.pressure += 1
    
    def openup(self, root, callback):
        q = deque([ root ])
        while q:
            node = q.pop()
            visit(self.spaceship, node, callback, q)

    def counter(self, count):
        count += 1

    def gateaction(self, node, closable, q):
        pass

    def travel(self, k):
        # while self.blocks:
        #     node = self.blocks.popleft()
        #     visit(self.spaceship, node, self.pressurised)
        self.openup(1, self.pressurised)
        while self.gates:
            gate = self.gates.pop()
            # self.openup(gate, self.gateaction)
            printdebug(gate)
            # self.gateaction(node)

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
        return self.gates_closed

# block 1 is depressurised first
spaceship = Spaceship(tree)
gates = spaceship.travel(k)
print(gates)
