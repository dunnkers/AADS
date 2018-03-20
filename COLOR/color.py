# Author: 		Jeroen Overschie
# S-number:		s2995697
# Date:			06-03-2018
# Challenge:	COLOR

import os
import sys
import math
from datetime import datetime
from queue import Queue
startTime = datetime.now()

# LOGGING
def printdebug(*s):
    if "TEST" in os.environ:
        print(*s)

# REDIRECT STDIN
if "TEST" in os.environ:
    old_stdin = sys.stdin
    sys.stdin = open('./COLOR/4.in')

def findColors(graph):
    red_colored = 0

    while len(graph) > 0:
        # since we only have 2 colors, we only have to invert. we choose True and
        # False since they're easy to invert.
        colors = {
            True: 0,  # a color, e.g. red
            False: 0  # a color, e.g. blue
        }

        def colorNode(node, color):
            colors[color] += 1
            neighbors = graph.pop(node)
            for neighbor in neighbors:
                if neighbor in graph:
                    colorNode(neighbor, not color)  # invert

        first = next(iter(graph.keys()))
        colorNode(first, True)
        red_colored += max(colors.values())  # possibly invert drawing
    
    return red_colored

t = int(input())
for _ in range(t):
    [m, n] = [int(x) for x in input().split()]
    graph = dict()
    # use generator to instantiate empty tuples in dict
    for i in range(n):
        a, b = [int(x) for x in input().split()]
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    lonely_vertices = m - len(graph)
    
    colors = findColors(graph)
    if colors:
        print(colors + lonely_vertices)
    else:
        print(-1)
