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
    __slots__ = ['idx', 'cost', 'factor', 'rem_cents', 'change', 'penalty']

    def __init__(self, idx, cost, factor):
        self.idx = idx
        self.cost = cost      # Ferry cost in cents
        self.factor = factor  # Discontent penalty factor
        self.rem_cents = cost % 100
        self.change = 100 - self.rem_cents
        self.penalty = self.change * factor

class Daniel(object):
    """Records Daniel's trips and money"""
    __slots__ = ['coins', 'discontent', 'paid']

    def __init__(self, coins):
        self.coins = coins
        self.discontent = 0
        # sort key is `penalty - change`; lowest penalty/highest gain come first
        self.paid = [] # priority queue

    def payWithChange(self, trip):
        printdebug('→ paying with change')
        self.coins += trip.change
        self.discontent += trip.penalty
        printdebug('coins +=', trip.change)
        printdebug('discontent +=', trip.penalty)
    
    def payFit(self, trip):
        printdebug('→ paying fit with coins')
        heapq.heappush(self.paid, (trip.penalty - trip.change, trip))
        self.coins -= trip.rem_cents
        printdebug('coins -=', trip.rem_cents)
    
    def revAndPayFit(self, trip, to_rev):
        printdebug('→ reverting ferry', to_rev.idx, 'to pay fit')
        self.payWithChange(to_rev)  # take penalty and change from to_rev
        heapq.heappop(self.paid)
        self.payFit(trip)

    def pay(self, trip):
        if trip.rem_cents == 0:
            printdebug('→ paying fit euros only')
        elif self.coins >= trip.rem_cents:  # pay fit with cents - no penalty
            self.payFit(trip)
        else:  # we need change
            shortage = trip.rem_cents - self.coins

            # is it more efficient to have paid somewhere else?
            pay = self.paid[0][1] if self.paid else None  # queue not empty
            # enough gain to fix shortage and a penalty advantage
            if pay and pay.change >= shortage and pay.penalty < trip.penalty:
                self.revAndPayFit(trip, pay)
            else:
                self.payWithChange(trip)

daniel = Daniel(m)

printdebug("FERRY")
printdebug(n, 'ferries')
printdebug(daniel.coins, 'coins')
printdebug('')

for i in range(n):
    trip = Trip(idx = i, cost=c[i], factor=d[i])
    printdebug('FERRY', i)
    daniel.pay(trip)
    printdebug('discontent =', daniel.discontent)
    printdebug('coins =', daniel.coins)
    printdebug('')
 
printdebug('discontent:')
print(daniel.discontent)
