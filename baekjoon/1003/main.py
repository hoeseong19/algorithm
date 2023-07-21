class Solution():
    def p1003(self, n):
        if n == 0:
            p1, p2 = 1, 0
        else:
            p1, p2 = 0, 1

            for _ in range(n-1):
                p1, p2 = p2, p1 + p2

        return [p1, p2]

n = int(input())
list_tc = [int(input()) for _ in range(n)]

for tc in list_tc:
    [print(p, end=" ") for p in Solution().p1003(tc)]

    print()

# print(Solution().p1003(0) == [1, 0])
# print(Solution().p1003(1) == [0, 1])
# print(Solution().p1003(3) == [1, 2])
# print(Solution().p1003(6) == [5, 8])
# print(Solution().p1003(22) == [10946, 17711])
