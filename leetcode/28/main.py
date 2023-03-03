class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


print(Solution().strStr(haystack="sadbutsad", needle="sad") == 0)
print(Solution().strStr(haystack="leetcode", needle="leeto") == -1)
