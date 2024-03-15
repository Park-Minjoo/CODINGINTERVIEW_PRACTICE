import sys
input = sys.stdin.readline
import math

def primenumber(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return x

def nextnumber(x):
    while True:
        if primenumber(x) == False:
            x += 1
        else:
            return x

times = int(input())
for _ in range(times):
    num = int(input())
    print(nextnumber(num))