# Author: 		Jeroen Overschie
# S-number:		s2995697
# Date:			05-03-2018
# Challenge:	LIBRARY
#
# The first line contains n — the number of items (1 ≤ n ≤ 105). The second line
# contains n numbers ai, (1 ≤ ai ≤ 105) — the identifiers of the items after 
# the attack.

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
    sys.stdin = open('./LIBRARY/1.in')

printdebug("LIBRARY")

n = int(input())

a = []
b = list(range(1, n + 1))
for num in input().split():
    ai = int(num)
    a.append(ai)
    if ai in b:
        b.remove(ai)

printdebug('n = ', n)
printdebug('a = ', a)
printdebug('b = ', b)

for i, ai in enumerate(a):
    if ai > n:
        a[i] = b[0] # first missing item
        b.pop(0)
        continue
    if i == 0:
        continue
    if ai != a[i - 1]:
        continue

    printdebug('next b is ', b[0])
    if ai < b[0]:
        printdebug('ok')
        a[i] = b[0]
    else:
        a[i - 1] = b[0]
    printdebug('same', ai, 'at idx', i)
    b.pop(0)

print(*a, sep=' ')