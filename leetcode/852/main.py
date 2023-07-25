from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        answer = 0

        length_arr = len(arr)

        start_index = 0
        end_index = length_arr - 1

        peak_index = length_arr // 2

        while peak_index:
            # arr[i - 1] < arr[i] > arr[i + 1]
            if (arr[peak_index - 1] < arr[peak_index]) and (arr[peak_index] > arr[peak_index + 1]):
                answer = peak_index
                break

            else:
                # arr[i - 1] < arr[i] < arr[i + 1]
                # to right
                if (arr[peak_index - 1] < arr[peak_index]) and (arr[peak_index] < arr[peak_index + 1]):
                    start_index = peak_index
                    peak_index = (peak_index + end_index) // 2

                # arr[i - 1] > arr[i] > arr[i + 1]
                # to left
                if (arr[peak_index - 1] > arr[peak_index]) and (arr[peak_index] > arr[peak_index + 1]):
                    end_index = peak_index
                    peak_index = (peak_index + start_index) // 2

        return answer


print(Solution().peakIndexInMountainArray(arr=[0, 1, 0]) == 1)
print(Solution().peakIndexInMountainArray(arr=[0, 2, 1, 0]) == 1)
print(Solution().peakIndexInMountainArray(arr=[0, 10, 5, 2]) == 1)