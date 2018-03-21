# Author: 		Jeroen Overschie
# S-number:		s2995697
# Date:			20-03-2018
# Challenge:	COLOR

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
    sys.stdin = open('./COLOR/2.in')

def color(graph):
    src = next(iter(graph.keys()))
    colored = {src: 1}
    colors = [0, 1]
    queue = [src]
    while queue:
        node = queue.pop()
        for adj in graph.pop(node):
            if not adj in colored:
                colored[adj] = 1 - colored[node]
                colors[colored[adj]] += 1
                queue.append(adj)
            elif adj == node:
                return -1 # self loop
            elif colored[adj] == colored[node]:  # not allowed
                return -1
    return max(colors)

def bipartite(graph):
    tot = 0
    while graph:
        clr = color(graph)
        if clr == -1:
            return -1        
        else:
            tot += clr
    
    return tot

t = int(input())
for _ in range(t):
    [m, n] = [int(x) for x in input().split()]
    graph = dict()
    # use generator to instantiate empty tuples in dict
    for i in range(n):
        a, b = [int(x) for x in input().split()]
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)

    islands = m - len(graph)
    colored = bipartite(graph)
    clr = colored + islands
    if colored != -1 and clr > 0:
        print(clr)
    else:
        print(-1)
