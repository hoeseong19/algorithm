import sys
from math import ceil, inf, log2
from typing import List

sys.setrecursionlimit(10**6)


class SegmentTree:
    def __init__(self, n: int):
        self.list_min_max = [[inf, -inf] for _ in range(pow(2, ceil(log2(n)) + 1))]

    def query(self, index: int, start: int, end: int, left: int, right: int):
        if right < start or end < left:
            return (inf, -inf)
        if left <= start and end <= right:
            return (self.list_min_max[index][0], self.list_min_max[index][1])

        min_num1, max_num1 = self.query(index * 2, start, (start + end) // 2, left, right)
        min_num2, max_num2 = self.query(index * 2 + 1, (start + end) // 2 + 1, end, left, right)

        return min(min_num1, min_num2), max(max_num1, max_num2)

    def update(self, index: int, start: int, end: int, target_index: int, value: int):
        if not (start <= target_index <= end):
            return

        self.list_min_max[index][0] = min(self.list_min_max[index][0], value)
        self.list_min_max[index][1] = max(self.list_min_max[index][1], value)

        if start == end:
            return

        self.update(index * 2, start, (start + end) // 2, target_index, value)
        self.update(index * 2 + 1, (start + end) // 2 + 1, end, target_index, value)


n, m = map(int, sys.stdin.readline().rstrip().split())
segment_tree = SegmentTree(n)
for i in range(n):
    value = int(sys.stdin.readline().rstrip())
    segment_tree.update(1, 0, n - 1, i, value)

for _ in range(m):
    start, end = map(int, sys.stdin.readline().rstrip().split())

    min_num, max_num = segment_tree.query(1, 0, n - 1, start - 1, end - 1)

    print(min_num, max_num)

# with open("./baekjoon/2357/input.txt", "r") as f:
#     n, m = map(int, f.readline().rstrip().split())
#     list_input_num = [int(f.readline().rstrip()) for _ in range(n)]
#     min_num, max_num = min(list_input_num), max(list_input_num)

#     for _ in range(m):
#         segment_tree = SegmentTree(n, list_input_num)
#         segment_tree.build(1, 0, n - 1)

#         start, end = map(int, f.readline().rstrip().split())

#         print(segment_tree.query(1, 0, n - 1, start - 1, end - 1) == list(map(int, f.readline().rstrip().split())))
