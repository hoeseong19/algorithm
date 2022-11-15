from collections import Counter
from heapq import heappop, heappush
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_counter = Counter(nums)
        heap = []

        for number in number_counter:
            heappush(heap, (-number_counter[number], number))

        return [heappop(heap)[1] for _ in range(k)]


solution = Solution()

print(solution.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2) == [1, 2])
print(solution.topKFrequent(nums=[1], k=1) == [1])
