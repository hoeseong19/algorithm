from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        answer = 0

        left, right = 0, len(nums) - 1

        while left <= right:
            targetIndex = left + ((right - left) // 2)

            if nums[targetIndex] < target:
                left = targetIndex + 1
            elif nums[targetIndex] > target:
                right = targetIndex - 1
            else:
                answer = targetIndex
                break

        answer = max(left, answer)

        return answer


print(Solution().searchInsert(nums=[1, 3, 5, 6], target=1) == 0)
print(Solution().searchInsert(nums=[1, 3, 5, 6], target=2) == 1)
print(Solution().searchInsert(nums=[1, 3, 5, 6], target=3) == 1)
print(Solution().searchInsert(nums=[1, 3, 5, 6], target=4) == 2)
print(Solution().searchInsert(nums=[1, 3, 5, 6], target=5) == 2)
print(Solution().searchInsert(nums=[1, 3, 5, 6], target=6) == 3)
print(Solution().searchInsert(nums=[1, 3, 5, 6], target=7) == 4)
