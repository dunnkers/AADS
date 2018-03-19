# Author: 		Jeroen Overschie
# S-number:		s2995697
# Date:			06-03-2018
# Challenge:	COLOR

import os
import sys
import math
from datetime import datetime
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
    colors = {}
    color_1 = 0
    color_2 = 0
    
    def check_neighbors(clr, vertices):
        return all(clr != colors.get(n) for n in vertices)

    for node, adj_vertices in graph.items():
        if check_neighbors(0, adj_vertices): # all neighbors are not color 0
            colors[node] = 0
            color_1 += 1
        elif check_neighbors(1, adj_vertices):  # all neighbors are not color 0
            colors[node] = 1
            color_2 += 1
        else:
            return None # cannot find any color for this vertex

    return max(color_1, color_2)

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
