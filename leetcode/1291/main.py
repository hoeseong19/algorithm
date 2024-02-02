from math import floor, log10
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        answer = []

        digits = "".join([str(i) for i in range(1, 10)])

        next_index = low // pow(10, floor(log10(low))) - 1
        next_length = floor(log10(low)) + 1

        if next_index + next_length > 9:
            next_index = 0
            next_length = next_length + 1

        target = int(digits[next_index : next_index + next_length])

        while target <= high and next_length < 10:
            if target >= low:
                answer.append(target)

            next_length = next_length + ((next_index + 1) // 10)
            next_index = (next_index + 1) % 10

            if next_index + next_length > 9:
                next_index = 0
                next_length = next_length + 1

            target = int(digits[next_index : next_index + next_length])

        return answer


# print(Solution().sequentialDigits(low=100, high=300) == [123, 234])
# print(Solution().sequentialDigits(low=1000, high=13000) == [1234, 2345, 3456, 4567, 5678, 6789, 12345])
print(Solution().sequentialDigits(low=10, high=1000000000) == [])
print(Solution().sequentialDigits(low=58, high=155) == [])
