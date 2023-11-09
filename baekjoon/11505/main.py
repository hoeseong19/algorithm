import sys
from math import ceil, log2

sys.setrecursionlimit(10**6)


class SegmentTree:
    def __init__(self, n: int, list_input_num):
        self.list_input_num = list_input_num
        self.list_product = [1 for _ in range(pow(2, ceil(log2(n)) + 1))]

    def build(self, index: int, start: int, end: int):
        if start == end:
            self.list_product[index] = self.list_input_num[start]
        else:
            self.build(index * 2, start, (start + end) // 2)
            self.build(index * 2 + 1, (start + end) // 2 + 1, end)
            for i in range(start, end + 1):
                self.list_product[index] = (self.list_product[index] * list_input_num[i]) % 1_000_000_007

    def query(self, index: int, start: int, end: int, left: int, right: int):
        if right < start or end < left:
            return 1

        if left <= start and end <= right:
            return self.list_product[index]

        value0 = self.query(index * 2, start, (start + end) // 2, left, right)
        value1 = self.query(index * 2 + 1, (start + end) // 2 + 1, end, left, right)

        return (value0 * value1) % 1_000_000_007

    def update(self, index: int, start: int, end: int, target_index: int, value: int):
        if not (start <= target_index <= end):
            return self.list_product[index]

        if start == end:
            self.list_product[index] = value % 1_000_000_007
            return self.list_product[index]

        value0 = self.update(index * 2, start, (start + end) // 2, target_index, value)
        value1 = self.update(index * 2 + 1, (start + end) // 2 + 1, end, target_index, value)

        self.list_product[index] = (value0 * value1) % 1_000_000_007

        return self.list_product[index]


n, m, k = map(int, sys.stdin.readline().rstrip().split())

list_input_num = [int(sys.stdin.readline().rstrip()) for i in range(n)]

segment_tree = SegmentTree(n, list_input_num)
segment_tree.build(1, 0, n - 1)

list_abc = [map(int, sys.stdin.readline().rstrip().split()) for _ in range(m + k)]

for a, b, c in list_abc:
    if a == 1:
        segment_tree.update(1, 0, n - 1, b - 1, c)
    if a == 2:
        print(segment_tree.query(1, 0, n - 1, b - 1, c - 1))

# with open("./baekjoon/11505/input.txt", "r") as f:
#     for _ in range(int(f.readline().rstrip())):
#         n, m, k = map(int, f.readline().rstrip().split())

#         segment_tree = SegmentTree(n)

#         list_input_num = [segment_tree.update(1, 0, n - 1, i, int(f.readline().rstrip())) for i in range(n)]

#         list_abc = [map(int, f.readline().rstrip().split()) for _ in range(m + k)]

#         for a, b, c in list_abc:
#             if a == 1:
#                 segment_tree.update(1, 0, n - 1, b - 1, c)
#             if a == 2:
#                 print(segment_tree.query(1, 0, n - 1, b - 1, c - 1) == int(f.readline().rstrip()))
