from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            mid = (left + right) // 2

            if left <= right:

                if nums[mid] > target:
                    return binary_search(left, mid - 1)
                elif nums[mid] < target:
                    return binary_search(mid + 1, right)
                else:
                    return mid
            else:
                return -1

        return binary_search(0, len(nums) - 1)


solution = Solution()

print(solution.search(nums=[-1, 0, 3, 5, 9, 12], target=9) == 4)
print(solution.search(nums=[-1, 0, 3, 5, 9, 12], target=2) == -1)
print(solution.search(nums=[-1, 0, 3, 5, 9, 12], target=13) == -1)
