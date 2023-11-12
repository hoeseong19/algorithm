import sys
from typing import List, Tuple


class DisjointSet:
    def __init__(self):
        self.root = {}

    def find(self, x: Tuple[int, int]):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: Tuple[int, int], y: Tuple[int, int]):
        rootX = self.find(x)
        rootY = self.find(y)

        self.root[rootY] = rootX


def solve(n: int, m: int, list2_arrow: List[List[str]]):
    disjoint_set = DisjointSet()

    for i in range(n):
        for j in range(m):
            next = (-1, -1)

            if (i, j) not in disjoint_set.root:
                disjoint_set.root[(i, j)] = (i, j)

            if list2_arrow[i][j] == "U":
                next = (i - 1, j)
            if list2_arrow[i][j] == "D":
                next = (i + 1, j)
            if list2_arrow[i][j] == "L":
                next = (i, j - 1)
            if list2_arrow[i][j] == "R":
                next = (i, j + 1)

            if next not in disjoint_set.root:
                disjoint_set.root[next] = next

            disjoint_set.union(next, (i, j))

    set_root = set()
    for i in range(n):
        for j in range(m):
            set_root.add(disjoint_set.find((i, j)))

    return len(set_root)


n, m = map(int, sys.stdin.readline().rstrip().split())

list2_arrow = []
for i in range(n):
    list2_arrow.append([])
    for _ in range(m):
        list2_arrow[i].append(sys.stdin.read(1))
    sys.stdin.read(1)

print(solve(n, m, list2_arrow))

# with open("./baekjoon/16724/input.txt", "r") as f:
#     for _ in range(int(f.readline().rstrip())):
#         n, m = map(int, f.readline().rstrip().split())

#         list2_arrow = []
#         for i in range(n):
#             list2_arrow.append([])
#             for _ in range(m):
#                 list2_arrow[i].append(f.read(1))
#             f.read(1)

#         print(solve(n, m, list2_arrow) == int(f.readline().rstrip()))
