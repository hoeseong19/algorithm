import sys
from typing import List


class Solution:
    def solve(self, n: int, m: int, list2_prefix_sum: List[List[int]], x1, y1, x2, y2) -> int:
        answer = 0

        answer = (
            list2_prefix_sum[x2][y2]
            + list2_prefix_sum[x1 - 1][y1 - 1]
            - list2_prefix_sum[x1 - 1][y2]
            - list2_prefix_sum[x2][y1 - 1]
        )

        return answer


# n, m = map(int, sys.stdin.readline().rstrip().split(" "))
# list_sum = [0 for _ in range(n)]
# list2_prefix_sum = [[0 for _ in range(n + 1)]]
# for _ in range(n):
#     sum = 0
#     list_prefix = [0]
#     for i, input_number in enumerate(sys.stdin.readline().rstrip().split(" ")):
#         int_number = int(input_number)
#         sum += int_number
#         list_prefix.append(list_sum[i] + sum)
#         list_sum[i] += sum
#     list2_prefix_sum.append(list_prefix)

# list2_xyxy = []
# for _ in range(m):
#     list2_xyxy.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))

# for x1, y1, x2, y2 in list2_xyxy:
#     print(Solution().solve(n, m, list2_prefix_sum, x1, y1, x2, y2))

with open("baekjoon/11660/input.txt", "r") as f:
    n_testcases = int(f.readline())
    for _ in range(n_testcases):
        n, m = map(int, f.readline().strip().split(" "))
        list_sum = [0 for _ in range(n)]
        list2_prefix_sum = [[0 for _ in range(n + 1)]]
        for _ in range(n):
            sum = 0
            list_prefix = [0]
            for i, input_number in enumerate(f.readline().strip().split(" ")):
                int_number = int(input_number)
                sum += int_number
                list_prefix.append(list_sum[i] + sum)
                list_sum[i] += sum
            list2_prefix_sum.append(list_prefix)

        list2_xyxy = []
        for _ in range(m):
            list2_xyxy.append(list(map(int, f.readline().strip().split(" "))))

        for x1, y1, x2, y2 in list2_xyxy:
            print(Solution().solve(n, m, list2_prefix_sum, x1, y1, x2, y2) == int(f.readline()))
