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

# LOGGING
# DEBUG_LEVEL = logging.DEBUG if "TEST" in os.environ else logging.CRITICAL
# logging.basicConfig(stream=sys.stderr, level=DEBUG_LEVEL)
# REDIRECT STDIN
if "TEST" in os.environ:
    old_stdin = sys.stdin
    sys.stdin = open('./STRING/3.in')

def printdebug(*s):
    if "TEST" in os.environ:
        print(*s)

printdebug("STRING")

s = list(input())
s_len = len(s)
s_mid = s_len // 2 + 1  # this number is negligible, skip it
printdebug(''.join(s))
printdebug('s_len: ', s_len)
printdebug('s_mid: ', s_mid)

m = int(input())
printdebug('m: %d' % m)


# a = [int(x) for x in input().split()]
# print(a)
# print(all_palindromes(a))

for a in input().split():
    aᵢ = int(a)

    if aᵢ == s_mid:
        printdebug('skipping')
        continue
    printdebug(aᵢ)

    l = aᵢ - 1
    r = s_len - aᵢ
    printdebug('[l = %d, r = %d]' % (l, r))

    s[l:r + 1] = reversed(s[l:r + 1])
    printdebug(''.join(s))

print(''.join(s))


