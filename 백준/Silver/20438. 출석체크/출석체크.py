import sys
input = sys.stdin.readline

n, k, q, m = map(int, input().split())
sleep = [False for _ in range(n+3)] # 조는 학생
for i in map(int, input().split()):
    sleep[i] = True # 조는 학생은 true

check = [1 for _ in range(n+3)] # 출석코드를 받은 학생
for i in range(3):
    check[i] = 0

for i in map(int, input().split()):
    if sleep[i]:
        continue
    for j in range(i, n+3, i): # i~n+2, step:i
        if sleep[j]:
            continue # 조는 학생의 배수는 제외
        check[j] = 0 # 나머지 배수는 체크했으므로 0으로 업데이트

sum = 0
for i in range(3, n+3):
    if check[i]:
        sum += 1
    check[i] = sum # 누적 합 구하기
# print("check: ", check)
for i in range(m):
    s, e = map(int, input().split())
    print(check[e] - check[s-1])