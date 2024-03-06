n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            # print("(", j, i, "), (", i, k, ")")
            # print(graph[j][i], graph[i][k])
            if graph[j][i] and graph[i][k]:
                # print("check, (", j, k, ")")
                graph[j][k] = 1


for g in graph:
    print(*g)