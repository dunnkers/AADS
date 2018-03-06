# Author: 		Jeroen Overschie
# S-number:		s2995697
# Date:			06-03-2018
# Challenge:	FERRY
#
# The first line contains two integers n and m, (1 ≤ n ≤ 3 · 105, 0 ≤ m ≤ 109) 
# representing the number of ferries on Daniel’s trip and the amount of 1-cent 
# coins at it’s beginning. The next two lines contain the prices for each of 
# the n ferry tickets and the discontent factors di of the 
# ferrymen (1 ≤ ci, di ≤ 105).

import os
import sys
import math
from queue import PriorityQueue
from collections import namedtuple
from datetime import datetime
startTime = datetime.now()

# LOGGING
def printdebug(*s):
    if "TEST" in os.environ:
        print(*s)

# REDIRECT STDIN
if "TEST" in os.environ:
    old_stdin = sys.stdin
    sys.stdin = open('./FERRY/2.in')

printdebug("FERRY")

n, m = [int(x) for x in input().split()]
printdebug('n', n, 'm', m)

c = [int(x) for x in input().split()]
d = [int(x) for x in input().split()]

# for num in input().split():
#     di = int(num)
#     # named tuple.....
# ferries = list(zip(c, d))
q = PriorityQueue()
Ferry = namedtuple('Ferry', 'total idx coins')
q.put(Ferry(0, 0, m))

least_disc = 10000000000 # 10^5 * 10^5 seems reasonably large
while not q.empty():
    item = q.get()
    printdebug('current ferry:', item)
    if item.idx == n: # ⚠️ Probably, this doesn't take the last penalty in account.
        least_disc = min(least_disc, item.total)
        continue
    cost = c[item.idx]                      # ferry cost
    discontent = d[item.idx]                # ferry discontent
    rem_cents = cost % 100
    if item.coins >= rem_cents:             # we can pay with cents
        coins = item.coins - rem_cents
        total = item.total
        idx = item.idx + 1
        q.put(Ferry(total, idx, coins))

    # if item.coins < rem_cents:              # we have to pay with euros
    change = 100 - rem_cents            # ferryman change
    coins = item.coins + change         # store in our wallet

    disc = change * discontent          # ferryman is not happy with change
    total = item.total + disc           # compute new total discontent

    idx = item.idx + 1
    q.put(Ferry(total, idx, coins))

    # pay either with 1-euros or cents
    



print(least_disc)
