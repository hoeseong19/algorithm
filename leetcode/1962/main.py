from heapq import heappop, heappush
from math import floor
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        answer = 0

        heap_piles = []

        for pile in piles:
            heappush(heap_piles, -pile)

        for _ in range(k):
            maximum_pile = heappop(heap_piles)

            heappush(heap_piles, floor(maximum_pile / 2))

        answer = sum(heap_piles) * -1

        return answer


solution = Solution()

print(solution.minStoneSum(piles=[5, 4, 9], k=2) == 12)
print(solution.minStoneSum(piles=[4, 3, 6, 7], k=3) == 12)
