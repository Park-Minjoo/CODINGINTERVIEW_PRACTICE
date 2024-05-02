import sys
input = sys.stdin.readline

N, K = map(int, input().split())
numbers = [0] * 1000001
end = 0
for _ in range(N):
    g, x = map(int, input().split())
    numbers[x] = g
    end = max(end, x)

step = 2 * K + 1
window = sum(numbers[:step])
answer = window

for i in range(step, end+1):
    window += numbers[i] - numbers[i-step]
    answer = max(answer, window)
print(answer)