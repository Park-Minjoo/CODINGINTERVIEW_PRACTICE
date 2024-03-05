n = int(input())
points = [0] * 301
for i in range(1, n+1):
    points[i] = int(input())
# print(points)
if n <= 2:
    print(sum(points))
else:
    dp = [0] * 301
    dp[1] = points[1]
    dp[2] = points[1] + points[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i-3] + points[i] + points[i-1], dp[i-2] + points[i])

    print(dp[n])

