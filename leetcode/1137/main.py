class Solution:
    def tribonacci(self, n: int) -> int:
        list_tribonacci_number = [0 for _ in range(max(n+1, 3))]
        list_tribonacci_number[0] = 0
        list_tribonacci_number[1] = 1
        list_tribonacci_number[2] = 1

        for i in range(3, n + 1):
            list_tribonacci_number[i] = list_tribonacci_number[i-1] + list_tribonacci_number[i-2] + list_tribonacci_number[i-3]

        return list_tribonacci_number[n]


print(Solution().tribonacci(n=0) == 0)
print(Solution().tribonacci(n=1) == 1)
print(Solution().tribonacci(n=2) == 1)
print(Solution().tribonacci(n=3) == 2)
print(Solution().tribonacci(n=4) == 4)
print(Solution().tribonacci(n=25) == 1389537)
