from functools import cache


class Solution:
    list2_movement = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]

    def knightDialer(self, n: int) -> int:
        @cache
        def getAvailableMovement(n: int, location: int) -> int:
            if n == 0:
                return 1
            else:
                available_movement = 0
                for num in self.list2_movement[location]:
                    available_movement = (available_movement + getAvailableMovement(n - 1, num)) % 1_000_000_007

                return available_movement

        available_movement = 0
        for i in range(10):
            available_movement = (available_movement + getAvailableMovement(n - 1, i)) % 1_000_000_007

        return available_movement


print(Solution().knightDialer(n=1) == 10)
print(Solution().knightDialer(n=2) == 20)
print(Solution().knightDialer(n=3131) == 136006598)
