from typing import List

from collections import defaultdict


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        answer = 0

        dict_num_TO_count = defaultdict(int)

        for num in nums:
            dict_num_TO_count[num] += 1

        for num, count in dict_num_TO_count.items():
            answer += sum(range(count)) if count >= 2 else 0

        return answer


print(Solution().numIdenticalPairs(nums=[1, 2, 3, 1, 1, 3]) == 4)
print(Solution().numIdenticalPairs(nums=[1, 1, 1, 1]) == 6)
print(Solution().numIdenticalPairs(nums=[1, 2, 3]) == 0)
