class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return 0 if n == 1 else int(self.kthGrammar(n - 1, (k + 1) // 2) ^ k % 2 == 0)
