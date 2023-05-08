from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        answer = 0

        length_mat = len(mat)

        l, r = 0, length_mat - 1

        for i in range(length_mat):
            if l == r:
                answer += mat[i][l]
            else:
                answer += mat[i][l]
                answer += mat[i][r]

            l += 1
            r -= 1

        return answer


print(Solution().diagonalSum(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 25)
print(Solution().diagonalSum(
    mat=[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == 8)
print(Solution().diagonalSum(mat=[[5]]) == 5)
