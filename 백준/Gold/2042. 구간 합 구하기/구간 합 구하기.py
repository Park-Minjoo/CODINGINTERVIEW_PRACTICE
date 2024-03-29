import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())

# maximum num of data : 1,000,000
arr = [0] * (n + 1)
tree = [0] * (n + 1)

# i번째 수까지: prefix sum
def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i & -i) # 0이 아닌 마지막 비트만큼 빼가면서 이동
        # print('prefix_sum:', i)
    return result

# i번째 수를 dif만큼 더함
def update(i, dif):
    while i <= n:
        tree[i] += dif
        i += (i & -i)
        # print(tree, i)

# start부터 end까지: prefix sum
def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start -1)

for i in range(1, n+1):
    x = int(input())
    arr[i] = x
    # print('i, x:', i, x)
    update(i, x)

for i in range(m+k):
    a, b, c = map(int, input().split())
    # update
    if a == 1:
        update(b, c - arr[b])
        arr[b] = c
    # interval sum
    else:
        print(interval_sum(b, c))