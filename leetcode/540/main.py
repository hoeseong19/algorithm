from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        answer = 0

        lengthNums = len(nums)

        if lengthNums == 1:
            answer = nums[0]
        else:
            left, right = 0, lengthNums - 1

            while left <= right:
                targetIndex = left + ((right - left) // 2)
                targetLeftIndex = targetIndex - 1
                targetRightIndex = (targetIndex + 1) % lengthNums

                if nums[targetIndex] == nums[targetLeftIndex]:
                    if targetIndex % 2 == 0:
                        right = targetIndex - 2
                    else:
                        left = targetIndex + 1

                elif nums[targetIndex] == nums[targetRightIndex]:
                    if targetIndex % 2 == 0:
                        left = targetIndex + 2
                    else:
                        right = targetIndex - 1

                else:
                    answer = nums[targetIndex]
                    break

        return answer


print(Solution().singleNonDuplicate(nums=[1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2)
print(Solution().singleNonDuplicate(nums=[3, 3, 7, 7, 10, 11, 11]) == 10)
print(Solution().singleNonDuplicate(nums=[1, 1, 2]) == 2)

