import sys
input = sys.stdin.readline

n = int(input())
files = dict()

for _ in range(n):
    extend = (input().split('.'))[1]
    if not extend in files:
        files[extend] = 1
    else:
        files[extend] += 1

s_files = sorted(files.items())

for key, value in s_files:
    print(key.rstrip(), value)