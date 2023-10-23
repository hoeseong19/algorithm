class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            return n % 4 == 0 and self.isPowerOfFour(n >> 2)


print(Solution().isPowerOfFour(n=-64) == False)
print(Solution().isPowerOfFour(n=-63) == False)
print(Solution().isPowerOfFour(n=16) == True)
print(Solution().isPowerOfFour(n=5) == False)
print(Solution().isPowerOfFour(n=1) == True)
print(Solution().isPowerOfFour(n=0) == False)
