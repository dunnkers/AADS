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

def visit(tree, node, visited=set()):
    visited.add(node)
    for neighbor, arg in tree[node].items():
        if neighbor in visited:
            continue
        yield neighbor, arg

class Spaceship(object):
    def __init__(self, spaceship):
        self.spaceship = spaceship
        self.pressure = 1
        self.gates_closed = 0

    def yield_edges(self, q):
        while q:
            v = q.pop()
            for w, closable in visit(self.spaceship, v):
                yield v, w, closable

    def check(self, k):
        return self.pressure + 1 > k

    def travel(self, k):
        gates = deque()
        q = deque([ 1 ])

        for _, w, closable in self.yield_edges(q):
            if closable:
                gates.append(w)
            elif self.pressure + 1 > k: # would explode
                printdebug('exploding at', w)
                return -1
            else:
                q.append(w)
                printdebug(w, closable)
                self.pressure += 1
        printdebug('→ initial pressure',self.pressure)

        full_potential = 0
        gateque = []
        while gates:
            gate = gates.pop()
            printdebug('GATE', gate)
            potential = 1
            if self.pressure + potential > k:
                printdebug('closing gate', gate, 'before inspection')
                self.gates_closed += 1
                continue
            gatequeue = deque([ gate ])
            for _, w, closable in self.yield_edges(gatequeue):
                potential += 1
                printdebug('🔶', w)
                if self.pressure + potential > k:
                    printdebug('closing gate', gate, 'on inspection at', w)
                    self.gates_closed += 1
                    break
                gatequeue.append(w)
            else: # if break was not triggered in `for`
                printdebug('gate', gate, 'has', potential, 'potential pressure')
                heappush(gateque, (-potential, gate))
                full_potential += potential
        # maxpress = self.pressure + full_potential
        # while maxpress > k:
        #     if not gateque:
        #         printdebug('this should not happen...')
        #         return -1
        #     potential, gate = heappop(gateque)
        #     potential *= -1
        #     maxpress -= potential
        #     self.gates_closed += 1
        while gateque:
            potential, gate = heappop(gateque)
            potential *= -1
            if self.pressure + full_potential > k:
                self.gates_closed += 1
                full_potential -= potential
                printdebug('closing gate', gate)
            else:  # leaving gate open
                printdebug('leaving open', gate)
                # self.pressure += potential
            printdebug('→ pressure', self.pressure)

        return self.gates_closed

# block 1 is depressurised first
spaceship = Spaceship(tree)
gates = spaceship.travel(k)
print(gates)
