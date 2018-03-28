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
for box in boxes:
    idx = bisect_left(bins, box)
    if idx == len(bins): # its bigger than last box
        bins.insert(idx, box) # same as append?
    else:
        bins[idx] = box # is sorting preserved now?!
print(len(bins))
