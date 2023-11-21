from collections import Counter
from typing import List


class Solution:
    def rev(self, num: int) -> int:
        reversed_num = 0

        while num != 0:
            digit = num % 10
            reversed_num = reversed_num * 10 + digit
            num //= 10

        return reversed_num

    def countNicePairs(self, nums: List[int]) -> int:
        answer = 0

        len_nums = len(nums)

        list_result = []

        for i in range(len_nums):
            list_result.append(nums[i] - self.rev(nums[i]))

        pair_counter = Counter(list_result)

        for v in pair_counter.values():
            answer += sum([i for i in range(1, v)])

        return answer % 1_000_000_007


print(Solution().countNicePairs(nums=[42, 11, 1, 97]) == 2)
print(Solution().countNicePairs(nums=[13, 10, 35, 24, 76]) == 4)
