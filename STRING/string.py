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
s_len = len(s)
s_mid = s_len // 2 + 1  # this number is negligible, skip it
printdebug('s_len: %d' % s_len)
printdebug('s_mid: %d' % s_mid)

m = int(input())
printdebug('m: %d' % m)

def revsection(ai):
    l = ai - 1
    r = s_len - ai
    s[l:r + 1] = reversed(s[l:r + 1])

counts = Counter()
for num in input().split():
    ai = int(num)
    if ai == s_mid:
        continue
    counts[ai] += 1

for ai in counts.items():
    if ai[1] % 2 == 1:
        revsection(ai[0])

print(''.join(s))


