import math
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        answer = 0

        count = 0

        left, right = 0, 0

        length = len(chars)

        while (left < length) and (right < length):
            if chars[left] == chars[right]:
                count += 1
                right += 1
            else:
                if count > 1:
                    chars[left+1:right] = str(count)

                    length = len(chars)

                    right = left + math.floor(math.log10(count)) + 2

                left = right

                count = 0

        if right == length:
            if count > 1:
                chars[left+1:right] = str(count)

                length = len(chars)

        answer = length

        return answer


print(Solution().compress(chars=["a", "a", "b", "b", "c", "c", "c"]) == 6)
print(Solution().compress(chars=["a"]) == 1)
print(Solution().compress(
    chars=["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]) == 4)
print(Solution().compress(
    chars=["a", "a", "a", "b", "b", "a", "a"]) == 6)
