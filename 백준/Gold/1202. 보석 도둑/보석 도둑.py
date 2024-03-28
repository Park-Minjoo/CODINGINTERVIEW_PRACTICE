import sys
input = sys.stdin.readline
import heapq

n, k = map(int, input().split())
jewels = []
for _ in range(n):
    heapq.heappush(jewels, list(map(int, input().split())))

weighs = []
for _ in range(k):
    weighs.append(int(input()))
weighs.sort()
# print(weighs)

answer = 0
tmp_jewels = []
for weigh in weighs:
    # print("aaaaaa", weigh)
    while jewels and weigh >= jewels[0][0]:
        # print("jewels: ", jewels, ", weigh: ", weigh, ", jewels[0][0]:", jewels[0][0])
        heapq.heappush(tmp_jewels, -heapq.heappop(jewels)[1])
        # print(tmp_jewels)
    if tmp_jewels:
        answer -= heapq.heappop(tmp_jewels)
        # print("answer: ", answer)
    elif not jewels:
        # print("not jewels: ", jewels)
        break

print(answer)
