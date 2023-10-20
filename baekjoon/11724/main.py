import sys
from collections import defaultdict, deque
from typing import Dict, List


def solve(n: int, graph: Dict[int, List[int]]) -> int:
    answer = 0

    # 각 노드의 방문 여부 리스트
    # 정점도 하나의 연결 요소
    list_visited = [False for _ in range(n)]

    # BFS
    q = deque([])
    for i in range(n):
        if list_visited[i]:
            continue
        answer += 1

        q.append(i)

        while q:
            node = q.popleft()

            for next_node in graph[node]:
                if list_visited[next_node]:
                    continue

                list_visited[next_node] = True
                q.append(next_node)

    return answer


# 정점의 개수 N과 간선의 개수 M
n, m = map(int, sys.stdin.readline().rstrip().split())

graph = defaultdict(list)

# 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.
for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())

    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

print(solve(n, graph))


# with open("baekjoon/11724/input.txt", "r") as f:
#     n_cases = int(f.readline().rstrip())

#     for _ in range(n_cases):
#         # 정점의 개수 N과 간선의 개수 M
#         n, m = map(int, f.readline().rstrip().split())

#         graph = defaultdict(list)

#         # 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.
#         for _ in range(m):
#             u, v = map(int, f.readline().rstrip().split())

#             graph[u - 1].append(v - 1)
#             graph[v - 1].append(u - 1)

#         print(solve(n, graph) == int(f.readline().rstrip()))
