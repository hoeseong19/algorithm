import sys


class Solution:
    def __init__(self, n, a, b):
        self.n = n
        self.a = a
        self.b = b

    def multiply(self, n, matrix1, matrix2):
        matrix3 = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    matrix3[i][j] += matrix1[i][k] * matrix2[k][j]
                    matrix3[i][j] %= 1_000

        return matrix3

    def solve(self, n, a, b):
        if b == 1:
            return a

        sub_answer = self.solve(n, a, b // 2)

        answer = self.multiply(n, sub_answer, sub_answer)

        if b % 2 == 1:
            answer = self.multiply(n, answer, a)

        return answer


n, b = map(int, sys.stdin.readline().rstrip().split())

a = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

answer = Solution(n, a, b).solve(n, a, b)

for i in range(n):
    for j in range(n):
        print(answer[i][j], end=" ")
    print()

# with open("./baekjoon/10830/input.txt", "r") as f:
#     for _ in range(int(f.readline().rstrip())):
#         n, b = map(int, f.readline().rstrip().split())

#         a = [list(map(int, f.readline().rstrip().split())) for _ in range(n)]

#         matrix3 = solve(n, b, a)

#         print(matrix3 == [list(map(int, f.readline().rstrip().split())) for _ in range(n)])
