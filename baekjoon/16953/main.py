import sys
from collections import deque


def solve(a, b) -> int:
    if a == b:
        return 0
    elif a > b:
        return -1
    else:
        q = deque([(a, 1)])

        while q:
            n, cnt = q.popleft()

            nn0 = n * 2
            nn1 = n * 10 + 1

            if nn0 == b:
                return cnt + 1
            if nn0 < b:
                q.append((nn0, cnt + 1))

            if nn1 == b:
                return cnt + 1
            if nn1 < b:
                q.append((nn1, cnt + 1))

    return -1


a, b = map(int, sys.stdin.readline().rstrip().split())
print(solve(a, b))

with open("./baekjoon/16953/input.txt", "r") as f:
    for _ in range(int(f.readline().rstrip())):
        a, b = map(int, f.readline().rstrip().split())
        print(solve(a, b) == int(f.readline().rstrip()))
