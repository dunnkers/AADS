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
    sys.stdin = open('./FERRY/4.in')

n, m = [int(x) for x in input().split()]

c = [int(x) for x in input().split()]
d = [int(x) for x in input().split()]

class Trip(object):
    """A trip is a ferry passing point"""
    __slots__ = ['cost', 'factor', 'penalty', 'avoided', 'gain']

    def __init__(self, cost, factor):
        self.cost = cost      # Ferry cost in cents
        self.factor = factor  # Discontent penalty factor
    
    def canPayFit(self, coins):
        return False

# CONST
EURO = 100
# VARS
discontent = 0
coins = m
trips = []
paid = [] # TODO sort this.

printdebug("FERRY")
printdebug(n, 'ferries')
printdebug(coins, 'coins')
printdebug('')

for i in range(n):
    trip = Trip(cost=c[i], factor=d[i])
    printdebug('FERRY', i)
    printdebug('cost', trip.cost, ', factor', trip.factor)

    # PAY
    rem_cents = trip.cost % EURO # left to pay after paying euros
    if rem_cents == 0: # euros only
        printdebug('→ paying fit euros only')
        trip.penalty = 0        # no penalty
    else:  # cents
        change = EURO - rem_cents
        penalty = change * trip.factor
        if coins >= rem_cents:  # pay fit - no penalty
            printdebug('→ paying fit with coins')
            trip.avoided = penalty
            trip.gain = change
            # paid.put((penalty, trip))
            paid.append(trip)
            # transaction
            coins -= rem_cents
            printdebug('coins -=', rem_cents)
        else:  # we need change

            # before paying the change - is it more efficient 
            # to have paid somewhere else?
            # ...
            shortage = rem_cents - coins
            reverted = False
            
            for pay in paid:
                # does it gain enough coins to buy next one and 
                # avoids enough discontent
                if pay.gain >= shortage and pay.avoided < penalty:
                    printdebug('→ reverting trip to be able to pay fit with coins!')
                    coins += pay.gain # get this coin we could've gained earlier
                    discontent += pay.avoided  # take this penalty instead
                    printdebug('coins +=', pay.gain)
                    printdebug('discontent +=', pay.avoided)
                    reverted = True
                    paid.remove(pay)
                    break

            # transaction
            if not reverted:
                trip.penalty = penalty
                printdebug('→ paying with change')
                coins += change
                discontent += trip.penalty
                printdebug('discontent +=', trip.penalty)
            else:  # ⚠️  SAME AS `paying fit with coins` scenario
                printdebug('→ paying fit with coins')
                trip.avoided = penalty
                trip.gain = change
                # paid.put((penalty, trip))
                paid.append(trip)
                # transaction
                coins -= rem_cents
                printdebug('coins -=', rem_cents)

    # WE TRAVELLED
    trips.append(trip)
    printdebug('discontent =', discontent)
    printdebug('coins =', coins)
    printdebug('')

printdebug('discontent:')
print(discontent)
quit()

# q = PriorityQueue()
# Ferry = namedtuple('Ferry', 'total idx coins')
# q.put(Ferry(0, 0, m))

# least_disc = 10000000000 # 10^5 * 10^5 seems reasonably large
# while not q.empty():
#     item = q.get()
#     printdebug('current ferry:', item)
#     if item.idx == n: # ⚠️ Probably, this doesn't take the last penalty in account.
#         least_disc = min(least_disc, item.total)
#         continue
#     cost = c[item.idx]                      # ferry cost
#     discontent = d[item.idx]                # ferry discontent
#     rem_cents = cost % 100
#     if item.coins >= rem_cents:             # we can pay with cents
#         coins = item.coins - rem_cents
#         total = item.total
#         idx = item.idx + 1
#         q.put(Ferry(total, idx, coins))

#     # if item.coins < rem_cents:              # we have to pay with euros
#     change = 100 - rem_cents            # ferryman change
#     coins = item.coins + change         # store in our wallet

#     disc = change * discontent          # ferryman is not happy with change
#     total = item.total + disc           # compute new total discontent

#     idx = item.idx + 1
#     q.put(Ferry(total, idx, coins))

#     # pay either with 1-euros or cents
    



# print(least_disc)
