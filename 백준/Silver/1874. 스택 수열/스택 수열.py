import sys
input = sys.stdin.readline

count = 1
temp = True
stack = []
op = []

N = int(input())
for _ in range(N):
    num = int(input())

    while count <= num: # num이하의 숫자까지 스택에 저장
        stack.append(count)
        op.append('+')
        count += 1

    if stack[-1] == num: # stack의 마지막이 num이면 제거
        stack.pop()
        op.append('-')
    else: # 스택 수열을 만들 수 없으므로 False
        temp = False
        break

# 스택 수열을 만들 수 있는지 여부에 따라 출력
if temp == False:
    print("NO")
else:
    for i in op:
        print(i)
