import sys
from collections import deque
from typing import List


def solve(ladder: List[int], snake: List[int]) -> int:
    answer = 0

    list_visited = [False for _ in range(101)]
    list_visited[1] = True

    q = deque([(1, 0)])

    while q:
        index, count = q.popleft()

        for next in range(0, min(6, 100 - index)):
            next_index = index + next + 1

            if list_visited[next_index]:
                continue

            if next_index == 100:
                return count + 1

            list_visited[next_index] = True

            if ladder[next_index] != -1:
                next_index = ladder[next_index]
            if snake[next_index] != -1:
                next_index = snake[next_index]

            list_visited[next_index] = True

            q.append((next_index, count + 1))

    return answer


# 사다리의 수 N(1 ≤ N ≤ 15)과 뱀의 수 M(1 ≤ M ≤ 15)
n, m = map(int, sys.stdin.readline().rstrip().split())
# N개의 줄에는 사다리의 정보를 의미하는 x, y (x < y)
ladder = [-1 for _ in range(101)]
for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    ladder[x] = y
# M개의 줄에는 뱀의 정보를 의미하는 u, v (u > v)
snake = [-1 for _ in range(101)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    snake[u] = v
print(solve(ladder, snake))

# with open("./baekjoon/16928/input.txt", "r") as f:
#     for _ in range(int(f.readline().rstrip())):
#         # 사다리의 수 N(1 ≤ N ≤ 15)과 뱀의 수 M(1 ≤ M ≤ 15)
#         n, m = map(int, f.readline().rstrip().split())
#         # N개의 줄에는 사다리의 정보를 의미하는 x, y (x < y)
#         ladder = [-1 for _ in range(101)]
#         for _ in range(n):
#             x, y = map(int, f.readline().rstrip().split())
#             ladder[x] = y
#         # M개의 줄에는 뱀의 정보를 의미하는 u, v (u > v)
#         snake = [-1 for _ in range(101)]
#         for _ in range(m):
#             u, v = map(int, f.readline().rstrip().split())
#             snake[u] = v
#         print(solve(ladder, snake) == int(f.readline().rstrip()))
