from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum([list(str) != sorted(list(str)) for str in zip(*strs)])

print(Solution().minDeletionSize(strs = ["cba","daf","ghi"]) == 1)
print(Solution().minDeletionSize(strs = ["a","b"]) == 0)
print(Solution().minDeletionSize(strs = ["zyx","wvu","tsr"]) == 3)
