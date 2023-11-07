import sys
from typing import List
from math import log2, ceil

sys.setrecursionlimit(10**6)


class SegmentTree:
    def __init__(self, n: int, list_input_num: List[int]):
        self.n = n
        self.list_input_num = list_input_num
        self.list_tree = [0 for _ in range(pow(2, ceil(log2(n)) + 1))]

        self.build(1, 0, n - 1)

    def build(self, index: int, start: int, end: int):
        if start == end:
            self.list_tree[index] = self.list_input_num[start]
        else:
            self.build(index * 2, start, (start + end) // 2)
            self.build(index * 2 + 1, (start + end) // 2 + 1, end)
            self.list_tree[index] = sum(self.list_input_num[start : end + 1])

    def find(self, index: int, start: int, end: int, left: int, right: int):
        if (left > end) or (right < start):
            return 0
        if (left <= start) and (end <= right):
            return self.list_tree[index]

        return self.find(index * 2, start, (start + end) // 2, left, right) + self.find(
            index * 2 + 1, (start + end) // 2 + 1, end, left, right
        )

    def update(self, index: int, start: int, end: int, target_index: int, value: int):
        if (start > target_index) or (target_index > end):
            return

        self.list_tree[index] += value - self.list_input_num[target_index]

        if start == end:
            return
        self.update(index * 2, start, (start + end) // 2, target_index, value)
        self.update(index * 2 + 1, (start + end) // 2 + 1, end, target_index, value)

        self.list_input_num[target_index] = value


n, m, k = map(int, sys.stdin.readline().rstrip().split())

list_n = []

for _ in range(n):
    num = int(sys.stdin.readline().rstrip())

    list_n.append(num)

segment_tree = SegmentTree(n, list_n)

list_abc = []
for _ in range(m + k):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())

    list_abc.append((a, b, c))

for a, b, c in list_abc:
    # 값 변경
    if a == 1:
        segment_tree.update(1, 0, n - 1, b - 1, c)

    # 합 구하기
    if a == 2:
        print(segment_tree.find(1, 0, n - 1, b - 1, c - 1))

# with open("./baekjoon/2042/input.txt", "r") as f:
#     for _ in range(int(f.readline().rstrip())):
#         n, m, k = map(int, f.readline().rstrip().split())

#         list_n = []

#         for _ in range(n):
#             num = int(f.readline().rstrip())

#             list_n.append(num)

#         segment_tree = SegmentTree(n, list_n)

#         list_abc = []
#         for _ in range(m + k):
#             a, b, c = map(int, f.readline().rstrip().split())

#             list_abc.append((a, b, c))

#         for a, b, c in list_abc:
#             # 값 변경
#             if a == 1:
#                 segment_tree.update(1, 0, n - 1, b - 1, c)

#             # 합 구하기
#             if a == 2:
#                 answer = segment_tree.find(1, 0, n - 1, b - 1, c - 1)
#                 print(answer == int(f.readline().rstrip()))
