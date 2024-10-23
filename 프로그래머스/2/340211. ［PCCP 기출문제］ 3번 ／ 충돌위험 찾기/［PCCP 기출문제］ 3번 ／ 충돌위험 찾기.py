def solution(points, routes):
    answer = 0
    n = len(routes)
    l = len(routes[0])
    idx = [0 for _ in range(n)]
    position = [[0,0] for _ in range(n)]
    complete = [0 for _ in range(n)]

    while 1:
        pos_check = set()
        conflict = set()
        if sum(complete) == n:
            break
        for robot in range(n):
            i = idx[robot]
            if i == 0:
                position[robot][0] = points[routes[robot][0]-1][0]
                position[robot][1] = points[routes[robot][0]-1][1]
            elif i == l:
                complete[robot] = 1
                idx[robot] += 1
                continue
            elif i > l:
                continue

            destination = points[routes[robot][i]-1]
            if position[robot][0] != destination[0]:
                move = 1 if position[robot][0] < destination[0] else -1
                position[robot][0] += move
            elif position[robot][1] != destination[1]:
                move = 1 if position[robot][1] < destination[1] else -1
                position[robot][1] += move
            if position[robot] == destination:
                idx[robot] += 1

            x, y = position[robot]
            if complete[robot]:
                continue
            if (x, y) in pos_check:
                conflict.add((x, y))
            else:
                pos_check.add((x, y))
        answer += len(conflict)
    return answer

# solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [2, 4]])