import sys
from collections import deque
from typing import Deque, List, Optional, Tuple


def solve(a: int, b: int) -> str:
    if a == b:
        return ""

    def D(num):
        return (num * 2) % 10000

    def S(num):
        return (num - 1) % 10000

    def L(num):
        quotient, remainder = num // 1000, num % 1000
        return remainder * 10 + quotient

    def R(num):
        quotient, remainder = num // 10, num % 10
        return remainder * 1000 + quotient

    list_visited: List[Optional[str]] = [None for _ in range(10000)]
    list_parent = [-1 for _ in range(10000)]

    q: Deque[int] = deque([a])

    list_visited[a] = ""

    while q and list_visited[b] is None:
        num = q.popleft()

        list_next = [(D(num), "D"), (S(num), "S"), (L(num), "L"), (R(num), "R")]

        for next_num, next_command in list_next:
            if list_visited[next_num] is not None:
                continue

            list_visited[next_num] = next_command
            list_parent[next_num] = num

            if next_num == b:
                break
            q.append(next_num)

    list_command = []

    parent = b
    while parent != -1:
        list_command.append(list_visited[parent])
        parent = list_parent[parent]

    return "".join(list_command[::-1])


n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(solve(a, b))

with open("./baekjoon/9019/input.txt") as f:
    n = int(f.readline().rstrip())
    for _ in range(n):
        a, b = map(int, f.readline().rstrip().split())
        print(solve(a, b))
