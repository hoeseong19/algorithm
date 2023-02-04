from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        answer = False

        length_s2 = len(s2)

        s1_counter = Counter(s1)

        left, right = 0, 0

        while right < length_s2:
            if s1_counter.get(s2[right], 0) > 0:
                s1_counter[s2[right]] -= 1

                if right - left + 1 == len(s1):
                    answer = True

                    break

                right += 1

            else:
                s1_counter[s2[left]] += 1

                left += 1

        return answer


print(Solution().checkInclusion(s1="ab", s2="eidbaooo") == True)
print(Solution().checkInclusion(s1="ab", s2="eidboaoo") == False)
print(Solution().checkInclusion(s1="adc", s2="dcda") == True)
print(Solution().checkInclusion(s1="hello", s2="ooolleoooleh") == False)
