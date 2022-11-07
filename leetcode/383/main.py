from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        return (Counter(ransomNote) - Counter(magazine)) == {}


solution = Solution()

print(solution.canConstruct(ransomNote="a", magazine="b") == False)
print(solution.canConstruct(ransomNote="aa", magazine="ab") == False)
print(solution.canConstruct(ransomNote="aa", magazine="aab") == True)
print(solution.canConstruct(ransomNote="aab", magazine="baa") == True)
