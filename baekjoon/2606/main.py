import sys
from collections import defaultdict, deque


def solve(n, graph):
    list_visited = [False for _ in range(n)]

    q = deque([0])
    list_visited[0] = True

    while q:
        com = q.popleft()

        next_coms = graph[com]
        for next_com in next_coms:
            if list_visited[next_com]:
                continue

            list_visited[next_com] = True
            q.append(next_com)

    return sum(list_visited) - 1


# 첫째 줄에는 컴퓨터의 수가 주어진다.
n = int(sys.stdin.readline().rstrip())
# 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다.
m = int(sys.stdin.readline().rstrip())

graph = defaultdict(list)
# 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.
for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())

    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

print(solve(n, graph))

# with open("baekjoon/2606/input.txt", "r") as f:
#     n_cases = int(f.readline().rstrip())
#     for _ in range(n_cases):
#         # 첫째 줄에는 컴퓨터의 수가 주어진다.
#         n = int(f.readline().rstrip())
#         # 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다.
#         m = int(f.readline().rstrip())

#         graph = defaultdict(list)
#         # 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.
#         for _ in range(m):
#             u, v = map(int, f.readline().rstrip().split())

#             graph[u - 1].append(v - 1)
#             graph[v - 1].append(u - 1)

#         print(solve(n, graph) == int(f.readline().rstrip()))
