from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        answer = 0

        costs.sort()

        left, right = 0, len(costs)

        sum_costs = sum(costs[left:right])

        while sum_costs > coins and left <= right:
            sum_costs -= costs[right-1]
            right -= 1

        answer = right - left

        return answer


print(Solution().maxIceCream(costs=[1, 3, 2, 4, 1], coins=7) == 4)
print(Solution().maxIceCream(costs=[10, 6, 8, 7, 7, 8], coins=5) == 0)
print(Solution().maxIceCream(costs=[1, 6, 3, 1, 2, 5], coins=20) == 6)
