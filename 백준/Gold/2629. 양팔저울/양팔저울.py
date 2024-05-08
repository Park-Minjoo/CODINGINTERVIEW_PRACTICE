import sys
input = sys.stdin.readline

n, w = int(input()), list(map(int, input().split()))
m, b = int(input()), list(map(int, input().split()))

# dp[사용한 추의 개수][추의 무게 차이]
dp = [[0 for _ in range((500 * j)+1)] for j in range(n+1)]
ans = []

def cal(num, weight): # 추로 판별할 수 있는 구슬의 무게를 나타내는 함수
    if num > n: # 사용할 수 있는 추의 개수를 넘어가면 종료
        return
    if dp[num][weight] == 1: # 이미 같은 추의 무게와 개수로 방문했다면 종료
        return
    dp[num][weight] = 1

    # 3가지 경우 수행
    cal(num+1, weight + w[num-1]) # 추의 무게를 더함
    cal(num+1, weight) # 추를 사용하지 않음
    cal(num+1, abs(weight - w[num-1])) # 추 다른 쪽에 넣기 (무게 빼기)

cal(0,0)

for bead in b:
    if bead > 500 * n:
        ans.append('N')
    elif dp[n][bead] == 1:
        ans.append('Y')
    else:
        ans.append('N')
print(*ans)