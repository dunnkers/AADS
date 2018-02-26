# Author: 		Jeroen Overschie
# S-number:		s2995697
# Date:			26-02-2018
# Challenge:	ANCESTORS
#
# The first line of the input contains the numbers N and M 
# (1 ≤ N ≤ 250000, 1 ≤ M ≤ 300000). The second line contains N integers A_i, 
# representing the ancestors of the members i. If a member doesn’t 
# have an ancestor, then Ai = 0. The following M lines represent the 
# queries (Pi, Qi) as described above.
#
# Time complexity: x
# n is .... Runs in ..., because
#
# Memory complexity: x
# Because, ...
#
# Submission link, for own ease of use:
# http: // themis.housing.rug.nl/course/2017-2018/aads/ancestors/python

import logging
import os
import sys
import math

# LOGGING
DEBUG_LEVEL = logging.DEBUG if "TEST" in os.environ else logging.CRITICAL
logging.basicConfig(stream=sys.stderr, level=DEBUG_LEVEL)
# REDIRECT STDIN
if "TEST" in os.environ:
    old_stdin = sys.stdin
    sys.stdin = open('./ANCESTORS/2.in')

logging.info("ANCESTORS")

n, m = [int(x) for x in input().split()]
ancestors = [int(x) for x in input().split()]
logging.debug('ancestors: %s' % ancestors)

prev = dict()
for _ in range(m):
    p, q = [int(x) for x in input().split()]
    logging.debug('p = %d, q = %d' % (p, q))
    idx = p - 1  # idx-1 to correct position to idx.
    for i in range(q):
        # check prev existance
        # key = prev.get()
        curr = ancestors[idx]
        if curr == 0:
            print(0)
            break
        if i == q - 1:
            print(curr)
            break
        # next
        idx = curr - 1 # idx-1 to correct pos to idx
