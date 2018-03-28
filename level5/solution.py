import collections
import fractions
import math

def answer(w, h, s):    
    lattice=0
    gcdSum = 0
    for cyclePartitionW in GetCyclePartitions(w):
        for cyclePartitionH in GetCyclePartitions(h):            
            cycleCount =GetCycleCount(cyclePartitionW, w)*GetCycleCount(cyclePartitionH, h)
            gcdSum = sum([sum([fractions.gcd(i, j) for i in cyclePartitionW]) for j in cyclePartitionH])
            lattice+=cycleCount*(s**gcdSum)
    permutations = (math.factorial(w)*math.factorial(h)) 
    return lattice//permutations

def GetCycleCount(z, x):
    permutations = math.factorial(x)
    for a, b in collections.Counter(z).items():
        permutations //=(a**b)*math.factorial(b)
    return permutations        

def GetCyclePartitions(x, i=1):
    yield [x]
    for i in range(i, x//2 + 1):
        for p in GetCyclePartitions(x-i, i):
            yield [i] + p

print(answer(2,2,2))
