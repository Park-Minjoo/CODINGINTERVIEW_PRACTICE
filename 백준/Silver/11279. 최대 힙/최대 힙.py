import sys
import heapq as hq
input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
    x = int(input())
    if x:
        hq.heappush(heap, (-x, x))
    else:
        if len(heap) >= 1:
            print(hq.heappop(heap)[1])
        else:
            print(0)

'''
Input
13
0
1
2
0
0
3
2
1
0
0
0
0
0

Output
0
2
1
3
2
1
0
0
'''