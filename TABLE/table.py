# Author: 		Jeroen Overschie
# S-number:		s2995697
# Date:			25-02-2018
# Challenge:	TABLE
# 
# The input for this program are three numbers n, m and k. The program
# then computes the k-th largest number in the multiplication table of
# up to n * m.

import logging
import os
import sys
import math

# LOGGING
DEBUG_LEVEL = logging.DEBUG if "TEST" in os.environ else logging.CRITICAL
logging.basicConfig(stream=sys.stderr, level=DEBUG_LEVEL)
# REDIRECT STDIN
if "TEST" in os.environ:
    old_stdin = sys.stdin  # save it, in case we need to restore it
    sys.stdin = open('./TABLE/2.in')

logging.info("TABLE")

def getKthLargestNumber(n, m, k):
    mplus = m + 1
    def isSufficient(x):
        count = 0
        for i in range(1, mplus):  # would be xrange in Python 2.x
            # use Python 3.x's `//` operator to obtain int
            count += min(x // i, n)
        return count >= k

    smallest, largest = 1, m * n
    while smallest < largest:
        # use Python 3.x's `//` operator to obtain int
        mi = (smallest + largest) // 2
        if not isSufficient(mi):
            smallest = mi + 1
        else:
            largest = mi
    return smallest

n, m, k = [int(x) for x in input().split()]

logging.debug('n = %d', n)
logging.debug('m = %d', m)
logging.debug('k = %d', k)

# The answer is printed normally
print(math.floor(getKthLargestNumber(n, m, k)))
