# Author: 		Jeroen Overschie
# S-number:		s2995697
# Date:			26-02-2018
# Challenge:	ANCESTORS
#
# The first line of the input contains the numbers N and M 
# (1 ≤ N ≤ 250000, 1 ≤ M ≤ 300000). The second line contains N integers A_i, 
# representing the ancestors of the members i. If a member doesn’t 
# have an ancestor, then Ai = 0. The following M lines represent the 
# queries (Pi, Qi) as described.

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

# key/value store of previously computed answers
prev = dict()

def findAncestor(p, q):
    stor = (p, q)
    for i in range(q):
        key = (p, q - i)
        if key in prev:
            val = prev.get(key)
            logging.debug('we had %s before; answer is %d' % (key, val))
            return val

        p = ancestors[p - 1]
        
        if p == 0:
            prev[stor] = 0
            return 0
    prev[stor] = p
    logging.debug('storing %s = %d' % (stor, p))
    return p

for _ in range(m):
    p, q = [int(x) for x in input().split()]
    logging.debug('p = %d, q = %d' % (p, q))
    print('%d' % findAncestor(p, q))
