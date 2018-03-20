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
    sys.stdin = open('./COLOR/5.in')

def findColors(graph):
    red_colored = 0
    any_cool_coloring = False

    while len(graph) > 0:
        # since we only have 2 colors, we only have to invert. we choose True and
        # False since they're easy to invert.
        colors = {
            True: 0,  # a color, e.g. red
            False: 0  # a color, e.g. blue
        }
        coloredNodes = {}

        def colorNode(node, color):
            colors[color] += 1
            coloredNodes[node] = color
            neighbors = graph.pop(node)
            for neighbor in neighbors:
                if neighbor in coloredNodes and coloredNodes[neighbor] == color:
                    return False
                if neighbor in graph:
                    colorNode(neighbor, not color)  # invert
            return True

        first = next(iter(graph.keys()))
        result = colorNode(first, True)
        if not result:
            return False
        if result:
            any_cool_coloring = True 
            red_colored += max(colors.values())  # possibly invert drawing
    
    if not any_cool_coloring:
        return False
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
