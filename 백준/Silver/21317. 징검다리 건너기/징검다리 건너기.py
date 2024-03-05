n = int(input())
energy = [list(map(int, input().split())) for _ in range(n-1)]
k = int(input())
if n == 1:
    print(0)
    exit()
elif n == 2:
    print(energy[0][0])
    exit()

dp = [0] * n
dp[1] = energy[0][0]
dp[2] = min(energy[0][0] + energy[1][0], energy[0][1])
for i in range(3, n):
    dp[i] = min(energy[i-1][0]+dp[i-1], energy[i-2][1] + dp[i-2])

result = dp[-1]
dp2 = dp[:]

# 기회 1번 사용
for i in range(0, n-3):
    if dp[i] + k < dp[i+3]:
        dp2[i+3] = dp[i] + k
    for j in range(i+4, n):
        dp2[j] = min(dp[j], dp2[j-1] + energy[j-1][0], dp2[j-2] + energy[j-2][1])
    if dp2[-1] < result:
        result = dp2[-1]
print(result)