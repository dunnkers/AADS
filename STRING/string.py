# Author: 		Jeroen Overschie
# S-number:		s2995697
# Date:			04-03-2018
# Challenge:	STRING
#
# The first line of the input contains your string s of length from 2 to 2 · 105
# characters, consisting of lowercase Latin letters. The second line contains a 
# single integer m (1 ≤ m ≤ 105) the number of days when you change the string. 
# The third line contains m queries ai (1 ≤ ai; 2 · ai ≤ ksk) the position from 
# which you start transforming the string on the i-th day.

import os
import sys
import math
from collections import Counter
from datetime import datetime
startTime = datetime.now()

# LOGGING
def printdebug(*s):
    if "TEST" in os.environ:
        print(*s)
# REDIRECT STDIN
if "TEST" in os.environ:
    old_stdin = sys.stdin
    sys.stdin = open('./STRING/4.in')

printdebug("STRING")

s = list(input())
m = int(input())
s_mid = m // 2 + 1  # this number is negligible, skip it
printdebug('s_len: %d' % m)
printdebug('s_mid: %d' % s_mid)
printdebug('m: %d' % m)

counts = Counter()
for num in input().split():
    ai = int(num)
    if ai == s_mid:
        continue
    counts[ai] += 1

for ai in counts.items():
    if ai[1] % 2 == 1:
        l = ai[0] - 1
        r = m - ai[0]
        s[l:r + 1] = reversed(s[l:r + 1])
        # s[l:r + 1] = s[l:r + 1][::-1]

print(''.join(s))
printdebug(datetime.now() - startTime)

