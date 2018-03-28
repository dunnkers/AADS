# Author: 		Jeroen Overschie
# S-number:		s2995697
# Date:			28-03-2018
# Challenge:	BOXES

import os
import sys
import math
from bisect import bisect_left

# LOGGING
def printdebug(*s):
    if "TEST" in os.environ:
        print(*s)

# REDIRECT STDIN
if "TEST" in os.environ:
    old_stdin = sys.stdin
    sys.stdin = open('./BOXES/1.in')

# SCAN INPUT
n = int(input())
boxes = [int(x) for x in input().split()]
bins = []

"""
Uses a bisection algorithm to determine quickly where to insert a box in the
sorted bins list. If a suitable bin is found, replace the bin by the box. Else, 
create a new bin. Because we do left-bisections, we can correctly replace the
old bin size by the new box size.
"""
for box in boxes:
    idx = bisect_left(bins, box)    # look for a bin or place to insert this box
    if idx == len(bins):            # this box is larger than any bin we have
        bins.insert(idx, box)       # create a new bin (same as append)
    else:
        bins[idx] = box             # replace bin by this new, smaller box
print(len(bins))
