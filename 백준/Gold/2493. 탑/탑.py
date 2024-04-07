import sys
input = sys.stdin.readline

n = int(input())
tops = list(map(int, input().split()))
answer = [0] * n
stack = []

for i in range(n):
    while stack:
        if tops[stack[-1][0]] < tops[i]: # 탑에 닿지 않는 경우 (뒤에서 부터)
            stack.pop() # 스택에서 제거
        else:
            answer[i] = stack[-1][0]+ 1 # 탑에 닿은 경우, 탑의 번호를 저장.
            break
    stack.append((i, tops[i])) # 처음, 탑에 닿은 경우 stack 에 추가
print(*answer)
