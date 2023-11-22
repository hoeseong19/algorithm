from queue import PriorityQueue
from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        answer = []

        list2_priority = PriorityQueue()

        for i, list_num in enumerate(nums):
            for j, num in enumerate(list_num):
                list2_priority.put(((i + j, j, i), num))

        while not list2_priority.empty():
            answer.append(list2_priority.get()[1])

        return answer


print(Solution().findDiagonalOrder(nums=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 4, 2, 7, 5, 3, 8, 6, 9])
print(
    Solution().findDiagonalOrder(nums=[[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]])
    == [1, 6, 2, 8, 7, 3, 9, 4, 12, 10, 5, 13, 11, 14, 15, 16]
)
print(Solution().findDiagonalOrder(nums=[[1, 2, 3, 4, 5, 6]]) == [1, 2, 3, 4, 5, 6])
