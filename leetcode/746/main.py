from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        answer = 0

        length_cost = len(cost)

        # memoization
        # list_min_cost = [cost[0], cost[1]]

        # for i in range(2, length_cost):
        #     list_min_cost.append(cost[i] + min(list_min_cost[i - 1], list_min_cost[i - 2]))

        # answer = min(list_min_cost[length_cost - 1], list_min_cost[length_cost - 2])

        # tabulation
        pp, p = cost[0], cost[1]

        for i in range(2, length_cost):
            pp, p = p, cost[i] + min(pp, p)

        answer = min(pp, p)

        return answer


print(Solution().minCostClimbingStairs(cost=[10, 15, 20]) == 15)
print(Solution().minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6)
