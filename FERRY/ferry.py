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
import heapq
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
    sys.stdin = open('./FERRY/4.in')

n, m = [int(x) for x in input().split()]

c = [int(x) for x in input().split()]
d = [int(x) for x in input().split()]

class Trip(object):
    """A trip is a ferry passing point"""
    __slots__ = ['cost', 'factor', 'penalty', 'change']

    def __init__(self, cost, factor):
        self.cost = cost      # Ferry cost in cents
        self.factor = factor  # Discontent penalty factor

# CONST
EURO = 100
# VARS
discontent = 0
coins = m
trips = []
# sort key is `penalty - change`; then the lowest penalty and highest 
# change/`gain` comes first
paid = [] # TODO sort this.

printdebug("FERRY")
printdebug(n, 'ferries')
printdebug(coins, 'coins')
printdebug('')

for i in range(n):
    trip = Trip(cost=c[i], factor=d[i])
    trips.append(trip)
    printdebug('FERRY', i)
    printdebug('cost', trip.cost, ', factor', trip.factor)

    # PAY
    rem_cents = trip.cost % EURO # left to pay after paying euros
    if rem_cents == 0: # euros only
        printdebug('→ paying fit euros only')
        trip.penalty = 0        # no penalty
        printdebug('')
        continue
    
    # cents
    change = EURO - rem_cents
    trip.change = change
    penalty = change * trip.factor
    trip.penalty = penalty

    if coins < rem_cents: # we need change
        shortage = rem_cents - coins

        # is it more efficient to have paid somewhere else?
        pay = paid[0][1] if paid else None # queue not empty
        # does it gain enough coins to buy next one and
        # avoids enough discontent
        if not pay or pay.change < shortage or pay.penalty >= penalty:
            printdebug('→ paying with change')
            coins += change
            discontent += trip.penalty
            printdebug('discontent +=', trip.penalty)
            # ... not added to heap??
            continue

        # pay.change >= shortage or pay.penalty < penalty
        printdebug('→ reverting trip to be able to pay fit with coins!')
        coins += pay.change  # get this coin we could've gained earlier
        discontent += pay.penalty  # take this penalty instead
        printdebug('coins +=', pay.change)
        printdebug('discontent +=', pay.penalty)
        heapq.heappop(paid)

    if coins >= rem_cents:  # pay fit - no penalty
        printdebug('→ paying fit with coins')
        heapq.heappush(paid, (penalty - change, trip))
        coins -= rem_cents
        printdebug('coins -=', rem_cents)

    # WE TRAVELLED
    printdebug('discontent =', discontent)
    printdebug('coins =', coins)
    printdebug('')

printdebug('discontent:')
print(discontent)
