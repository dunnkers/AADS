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

# key/value store of previously computed answers
# prev = dict()


def findAncestor(p, q, i):
    for _ in range(q):
        p = ancestors[p - 1]
        if p == 0:
            return 0
    return p
    
    # STORING EVERY INTERMEDIATE STEP
    # key = (p, q - i)
    # if key in prev:
    #     val = prev.get(key)
    #     logging.debug('we had %d before; answer is %d' % (p, val))
    #     return val

    # prev[key, q - i] = findAncestor(p, q, i + 1)
    # return prev[key, q - i]

for _ in range(m):
    p, q = [int(x) for x in input().split()]
    logging.debug('p = %d, q = %d' % (p, q))
    print(findAncestor(p, q, 0))

    # STORING ONLY QUERIES
    # key = (p, q)
    # if key in prev:
    #     val = prev.get(key)
    #     logging.debug('we had %d before; answer is %d' % (p, val))
    #     print(val)
    # else:
    #     val = findAncestor(p, q, 0)
    #     print(val)
    #     prev[p, q] = val

    # FOR LOOP APPROACH
    # answer = -1
    # for i in range(q):
    #     p -= 1 # idx-1 to correct pos to idx

    #     val = prev.get(p)
    #     if val:
    #         logging.debug('we had %d before; answer is %d' % (p, val))
    #         pass

    #     p = ancestors[p]
    #     if p == 0:
    #         answer = 0
    #         break
    #     if i == q - 1: # at the very end of the loop
    #         answer = p
    #         break

    # print(answer)

# logging.debug(prev)
