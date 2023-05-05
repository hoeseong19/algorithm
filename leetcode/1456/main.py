class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        answer = 0

        length_s = len(s)

        list_vowel_letter = ['a', 'e', 'i', 'o', 'u']

        index_start, index_end = 0, k

        count_vowel_letter = 0

        for letter in s[index_start:index_end]:
            if letter in list_vowel_letter:
                count_vowel_letter += 1

        index_start += 1
        index_end += 1

        answer = max(answer, count_vowel_letter)

        while index_end <= length_s:
            if s[index_start-1] in list_vowel_letter:
                count_vowel_letter -= 1

            if s[index_end-1] in list_vowel_letter:
                count_vowel_letter += 1

            answer = max(answer, count_vowel_letter)

            index_start += 1
            index_end += 1

        return answer


print(Solution().maxVowels(s="abciiidef", k=3) == 3)
print(Solution().maxVowels(s="aeiou", k=2) == 2)
print(Solution().maxVowels(s="leetcode", k=3) == 2)
