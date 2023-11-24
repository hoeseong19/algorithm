from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        answer = 0

        piles.sort()

        for i in range(len(piles) // 3, len(piles), 2):
            answer += piles[i]

        return answer


print(Solution().maxCoins([2, 4, 1, 2, 7, 8]) == 9)
print(Solution().maxCoins([2, 4, 5]) == 4)
print(Solution().maxCoins([9, 8, 7, 6, 5, 1, 2, 3, 4]) == 18)
