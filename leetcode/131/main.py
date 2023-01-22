from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []

        def dividePalindrome(s, list_prev_palindrome):
            length = len(s)

            if length == 0:
                answer.append(list_prev_palindrome)
            else:
                for i in range(1, length+1):
                    cur_s = s[:i]

                    # Palindrome
                    if cur_s == cur_s[::-1]:
                        dividePalindrome(s[i:], [*list_prev_palindrome, cur_s])

        dividePalindrome(s, [])

        return answer


print(Solution().partition(s="aab") == [["a", "a", "b"], ["aa", "b"]])
print(Solution().partition(s="a") == [["a"]])
