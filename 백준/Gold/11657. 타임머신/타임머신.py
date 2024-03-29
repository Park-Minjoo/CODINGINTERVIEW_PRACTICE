import sys
input = sys.stdin.readline
INF = int(1e9) # 10억

n, m = map(int, input().split())
edges = [] # for all edges
distance = [INF] * (n+1) # initialize shortest distance table to INF

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c)) # a->b, cost: c
def bf(start):
    distance[start] = 0 # initialize the starting point
    for i in range(n): # repeat 0~n-1 round
        for j in range(m): # check all edges for every round
            # print(i, j)
            cur_node = edges[j][0]
            next_node = edges[j][1]
            edge_cost = edges[j][2]
            # if a shorter distance to another node th/ the cur_node
            if distance[cur_node] != INF and \
                    distance[next_node] > distance[cur_node] + edge_cost:
                distance[next_node] = distance[cur_node] + edge_cost
                # print('hey', cur_node, next_node, edge_cost, 'cost:', distance[next_node])
                if i == n-1: # negative cycle (for n-th round)
                    return True
    return False

# Bellman-Ford algorithm
negative_cycle = bf(1) # start: 1st node

if negative_cycle: # True
    print("-1")
else: # False
    for i in range(2, n+1): # except 1st node, for every nodes
        if distance[i] == INF: # not reachable
            print("-1")
        else:
            print(distance[i]) # reachable
