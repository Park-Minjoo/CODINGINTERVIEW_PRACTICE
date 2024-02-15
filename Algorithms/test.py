row, col = map(int, input().split())
arr = [list(input()) for _ in range(row)] # input
new = [] # new array

# 방항 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(row):
    for j in range(col):
        if arr[i][j] == 'X': # 땅이면 인접한 세 칸이상이 바다인지 확인
            count = 0 # 카운트는 X를 만날 때마다 초기화 되어야 함
            for k in range(4): # 4개 다 확인하기
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < row and 0 <= ny < col:
                    if arr[nx][ny] == '.':
                        count += 1
                else:
                    count += 1 # 범위를 벗어날 때
                    continue
            if count >= 3:
                new.append((i, j))

# . 으로 바꾸기
if len(new) > 0:
    for x, y in new:
        arr[x][y] = '.'

x1 = 0
y1 = col - 1
x2 = 0
y2 = 0

# 지도 범위 구하기

# x의 시작값
for i in range(row):
    if 'X' in arr[i]:
        x1 = i
        break

# x의 마지막 값
for i in range(row-1, -1, -1):
    if 'X' in arr[i]:
        x2 = i
        break

# y값 ----> ***이게 너무 어려움
for i in range(x1, x2 + 1): # 1 -> .X.
    for j in range(col): # 3
        if arr[i][j] == 'X': # arr[2][1]
            y1 = min(y1, j) # min(2, 1) = 1
            y2 = max(y2, j) # max(0, 1) = 1