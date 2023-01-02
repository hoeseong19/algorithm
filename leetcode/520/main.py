class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.islower() or word.isupper() or word.istitle()


print(Solution().detectCapitalUse(word="USA") == True)
print(Solution().detectCapitalUse(word="FlaG") == False)
