from collections import deque
import sys, copy
input = sys.stdin.readline

n, m = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(n)]
tmp_space = copy.deepcopy(space)

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def check(row, col):
    return row < 0 or row >= n or col < 0 or col >= m

def init():
    obj = deque()
    answer = 0
    for i in range(n):
        for j in range(m):
            if space[i][j] != 6 and space[i][j] != 0:
                obj.append((space[i][j], i, j))
            if space[i][j] == 0: answer += 1
    return obj, answer

cctv, answer = init()

def move(y, x, direction):
    direction %= 4
    while True:
        y += dy[direction]
        x += dx[direction]
        if check(y, x) or tmp_space[y][x] == 6:
            return
        if tmp_space[y][x] != 0:
            continue
        tmp_space[y][x] = '#'

for i in range(4**len(cctv)):
    case = i
    tmp_space = copy.deepcopy(space)

    for j in range(len(cctv)):
        d = case % 4
        case //= 4

        num, y, x = cctv[j]

        if num == 1:
            move(y, x, d)
        elif num == 2:
            move(y, x, d); move(y, x, d+2)
        elif num == 3:
            move(y, x, d); move(y, x, d + 1)
        elif num == 4:
            move(y, x, d);move(y, x, d + 1); move(y, x, d+2)
        else:
            move(y, x, d); move(y, x, d + 1); move(y, x, d + 2); move(y, x, d + 3)
    zero_cnt = 0
    for i in tmp_space:
        zero_cnt += i.count(0)
    answer = min(zero_cnt, answer)
print(answer)
