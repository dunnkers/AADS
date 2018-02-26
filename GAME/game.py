# Author: 		Jeroen Overschie
# S-number:		s2995697
# Date:			25-02-2018
# Challenge:	GAME
# 
# The input for this program is a number n on the first line, with n numbers on
# the second line. All input numbers are between 1 and 10 ^ 5.

import logging
import os
import sys
import math
from collections import Counter

# LOGGING
DEBUG_LEVEL = logging.DEBUG if "TEST" in os.environ else logging.CRITICAL
logging.basicConfig(stream=sys.stderr, level=DEBUG_LEVEL)
# REDIRECT STDIN
if "TEST" in os.environ:
    old_stdin = sys.stdin  # save it, in case we need to restore it
    sys.stdin = open('./GAME/3.in')

logging.info("GAME")

n = int(input()) # not actually needed because of Python

# Here, we use a Counter object. This is a handy built-in data structure,
# inherited from the `dict` data structure.
counts = Counter()
for s in input().split():
    num = int(s)
    counts[num] += num

logging.debug(counts)

points = 0
while True:
    item = counts.most_common(1)
    if not item:
        break
    num = item[0][0]
    counts.pop(num - 1, None)  # pop neighbors, but only if they exist
    counts.pop(num + 1, None)  # (hence `None` as default value)
    counts[num] -= num
    points += num # add value to points total
    if counts[num] == 0:
        del counts[num]
    # points += counts.pop(num)  # add value to points total

    logging.debug('popping %s' % item)

print(points)
