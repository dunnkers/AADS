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
bins = [] # sort from big to small # descending
# uses a bisection algorithm to determine quickly where to insert a box in the
# sorted bins list. if a suitable bin is found, replace the bin by the box. 
# else, create a new bin.
for box in boxes:
    idx = bisect_left(bins, box)
    if idx == len(bins): # its bigger than last box
        bins.insert(idx, box) # same as append?
    else:
        bins[idx] = box # is sorting preserved now?!
print(len(bins))
