r, c = map(int, input().split())
array = [] # 지도
for _ in range(r):
    array.append(list(input()))
# print(array)
# 상하좌우 확인하기
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

sink = [] # 잠기게 되는 좌표들의 배열
for i in range(r):
    for j in range(c):
        if array[i][j] == 'X': # 땅이면 인접 세칸 이상이 바다인지 확인하기
            count = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < r and 0 <= ny < c:
                    if array[nx][ny] == '.':
                        count += 1 # 인접한 칸 중 바다 개수 세주기
                else:
                    count += 1
                    print(count)
                    continue
            if count >= 3:
                sink.append((i, j))

# 바다로 바꾸기
if len(sink) > 0:
    for x, y in sink:
        array[x][y] = '.'
print(array)

x1 = 0
y1 = c-1
x2 = 0
y2 = 0
# 지도 범위 구하기
for i in range(0, r):
    if 'X' in array[i]:
        x1 = i
        break
for i in range(r-1, -1, -1):
    if 'X' in array[i]:
        x2 = i
        break

for i in range(x1, x2+1):
    for j in range(c):
        if array[i][j] == 'X':
            y1 = min(y1, j)
            y2 = max(y2, j)

# 정답 출력하기
for i in range(x1, x2+1):
    for j in range(y1, y2+1):
        print(array[i][j], end='')
    print()