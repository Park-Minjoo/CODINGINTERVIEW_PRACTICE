import sys
input = sys.stdin.readline
from collections import defaultdict

n, w = map(int, input().split())
tree = defaultdict(list)
for i in range(n-1):
    u, v = list(map(int, input().split()))
    tree[u].append(v)
    tree[v].append(u)

leaf_count = 0
for root, nodes in tree.items():
    if root != 1 and len(nodes) == 1:
        leaf_count += 1

print(round(w/leaf_count, 10))
