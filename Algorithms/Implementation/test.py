row, col = map(int, input().split())
arr = [list(input().split()) for _ in range(row)]
new = [ ['.' for i in range(col)] for j in range(row)]
# print(new)

steps = [(-1, 0), (0, -1), (1,0), (0, 1)]



for i in range(row):
    for j in range(col):
        if arr[i][j] == 'X':
            # print(i, j, arr[i][j])
            count = 0
            for step in steps:
                next_row = i + step[0]
                next_col = j + step[1]
                # print(next_row, next_col, arr[next_row][next_col])
                if arr[next_row][next_col] == '.' or \
                        next_row < 0 or next_col < 0 or \
                        next_row > row or next_col > col:
                    count += 1
            # print(count)
            if count < 3:
                # print(new[i][j], arr[i][j])
                new[i][j] = 'X'

print('arr')
for i in range(row):
    print(arr[i])

print('new')
for i in range(row):
    print(new[i])
#%%
