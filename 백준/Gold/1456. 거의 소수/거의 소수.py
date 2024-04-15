# 에라토스테네스의 체
import sys, math
input = sys.stdin.readline

a, b = map(int, input().split())
prime = [True] * (int(math.sqrt(b))+1)
prime[1] = False

for i in range(2, int(math.sqrt(b))+1):
    if prime[i]:
        if i * i > int(math.sqrt(b)):
            break
        for j in range(i**2, int(math.sqrt(b)) + 1, i):
            prime[j] = False

# for i in range(2, b):
#     if(prime[i]): print(i)
count = 0
for i in range(2, len(prime)):
    if prime[i]:
        res = i * i
        while True:
            if res < a:
                res *= i
                continue
            if res > b:
                break
            res *= i
            count += 1
print(count)

'''
Input
1 1000
Output
25

Input2
1 10
Output2
3

Input3
5324 894739
Output3
183
'''