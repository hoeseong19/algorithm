class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        answer = False

        length_s = len(s)

        for window_size in range(1, length_s//2+1):
            if length_s % window_size != 0:
                continue

            set_sub_s = set()

            for j in range(length_s // window_size):
                sub_s = s[window_size*j:window_size*(j+1)]

                set_sub_s.add(sub_s)

            answer = len(set_sub_s) == 1

            if answer:
                return answer

        return answer


print(Solution().repeatedSubstringPattern(s="abab") == True)
print(Solution().repeatedSubstringPattern(s="aba") == False)
print(Solution().repeatedSubstringPattern(s="abcabcabcabc") == True)
print(Solution().repeatedSubstringPattern(s="ababab") == True)
