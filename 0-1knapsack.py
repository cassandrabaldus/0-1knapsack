import collections
import numpy as np
from operator import itemgetter, attrgetter, methodcaller
import time

def dynamic (items, maxWeight) :
    x, y = len(items), maxWeight + 1
    V = np.zeros(shape=(x, y))
    w = maxWeight

    for i in range(1, x):
        for j in range(1, y):
            if items[i].weight > j:
                V[i][j] = V[i-1, j]
            else:
                V[i][j] = max(V[i-1][j], items[i].value + V[i-1][j-items[i].weight])

    return V[x-1][w];

def greedy1 (items, maxWeight) :
    sorted(items, key=attrgetter('weight'))
    totalValue = 0
    totalWeight = 0
    i = 0
    while totalWeight <= maxWeight :
        totalWeight += items[i].weight
        totalValue += items[i].value
        i += 1
    return totalValue

def greedy2 (items, maxWeight) :
    sorted(items, key=attrgetter('value'), reverse = True)
    totalValue = 0
    totalWeight = 0
    i = 0
    while totalWeight <= maxWeight:
        totalWeight += items[i].weight
        totalValue += items[i].value
        i += 1
    return totalValue


Item = collections.namedtuple('Item', ["weight", "value"])
alpha = Item(3, 100)
beta = Item(2, 20)
gamma = Item(4, 60)
delta = Item(1, 40)

item = [alpha, beta, gamma, delta]

dptimes = []
g1times = []
g2times = []
g1err = []
g2err = []

iterations  = 0

while iterations <= 100 :
    start = time.clock()
    dpvalue = dynamic(item, 5)
    end = time.clock()
    dptimes.append(end - start)

    start  = time.clock()
    g1value = greedy1(item, 5)
    end = time.clock()
    g1times.append(end - start)
    g1err.append((dpvalue - g1value) / dpvalue)

    start = time.clock()
    g2value = greedy2(item, 5)
    end = time.clock()
    g2times.append(end - start)
    g2err.append((dpvalue - g2value) / dpvalue)

    iterations += 1

iterations = 100
dpTotal = 0
g1Total = 0
g2Total = 0

for num in dptimes:
    dpTotal += num

for num in g1times:
    g1Total += num

for num in g2times:
    g2Total += num

dpAvg = dpTotal / iterations
g1Avg = g1Total / iterations
g2Avg = g2Total / iterations

print(dpAvg)
print(g1Avg)
print(g2Avg)