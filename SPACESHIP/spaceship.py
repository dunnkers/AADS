# Author: 		Jeroen Overschie
# S-number:		s2995697
# Date:			21-03-2018
# Challenge:	SPACESHIP

import os
import sys
import math
from collections import deque
from heapq import heappush, heappop

# LOGGING
def printdebug(*s):
    if "TEST" in os.environ:
        print(*s)

# REDIRECT STDIN
if "TEST" in os.environ:
    old_stdin = sys.stdin
    sys.stdin = open('./SPACESHIP/myown2.in')

# SCAN INPUT
[n, k] = [int(x) for x in input().split()]
tree = {}
for _ in range(n - 1):  # scan weighted edges
    [a, b, c] = [int(x) for x in input().split()]
    tree.setdefault(a, {})
    tree.setdefault(b, {})
    tree[a][b] = bool(c)
    tree[b][a] = bool(c)

class Spaceship(object):
    def __init__(self, spaceship, k):
        self.spaceship = spaceship
        self.k = k
        self.pressure = 1
        self.gates_closed = 0

    def yield_edges(self, q, visited=set()):
        while q:
            v = q.pop()
            visited.add(v)
            for w, closable in self.spaceship[v].items():
                if w in visited:
                    continue
                yield w, closable

    def check(self, potential):
        return self.pressure + potential > self.k
    
    
    def find_potential(self, gate):
        potential = 1
        q = deque([ gate ])
        for w, _ in self.yield_edges(q):
            potential += 1
            if self.check(potential):
                printdebug('closing gate', gate, 'on inspection at', w)
                self.gates_closed += 1
                return None
            q.append(w)
        printdebug('gate', gate, 'has', potential, 'potential pressure')
        return potential

    def travel(self):
        # EXPLORE ALL NODES BEFORE GATES & GATE POTENTIAL
        full_potential = 0
        gateque = []
        q = deque([1])
        for w, closable in self.yield_edges(q):
            if closable:
                potential = self.find_potential(w)
                if potential:
                    full_potential += potential
                    heappush(gateque, (potential * -1, w))  # *-1 for max-heap
            elif self.check(1):  # would explode
                printdebug('exploding at', w)
                return -1
            else:
                q.append(w)
                self.pressure += 1
        printdebug('→ initial pressure', self.pressure)

        # EXPLORE HOW MANY GATES WE MINIMALLY HAVE TO CLOSE
        while gateque:
            potential, gate = heappop(gateque)
            potential *= -1 # revert back to positive no
            if self.check(full_potential):
                self.gates_closed += 1
                full_potential -= potential
                printdebug('closing gate', gate)
            else:  # leaving gate open
                printdebug('leaving open', gate)

        return self.gates_closed

spaceship = Spaceship(tree, k)
gates = spaceship.travel()
print(gates)
