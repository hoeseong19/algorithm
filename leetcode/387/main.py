from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        answer = -1

        counter = Counter(s)

        length_s = len(s)

        for i in range(length_s):
            if counter.get(s[i]) == 1:
                answer = i

                break

        return answer
