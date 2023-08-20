from typing import List
from collections import deque

INDEX_X = 0
INDEX_Y = 1
INDEX_DIS = 2
INDEX_PREV_X = 3
INDEX_PREV_Y = 4


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        answer: List[List[int]] = []

        length_mat_x = len(mat)
        length_mat_y = len(mat[0])

        def bfs(x, y):
            max_dis = 0

            queue = deque([[x, y, max_dis, x, y]])

            while queue:
                next_x, next_y, dis, prev_x, prev_y = queue.popleft()

                value = mat[next_x][next_y]

                max_dis = dis

                if value == 0:
                    break

                if next_x-1 >= 0 and \
                        dis < length_mat_x + length_mat_y and \
                        (next_x-1, next_y) != (prev_x, prev_y):
                    queue.append([next_x-1, next_y, dis+1, next_x, next_y])
                if next_x+1 < length_mat_x and \
                        dis < length_mat_x + length_mat_y and \
                        (next_x+1, next_y) != (prev_x, prev_y):
                    queue.append([next_x+1, next_y, dis+1, next_x, next_y])
                if next_y-1 >= 0 and \
                        dis < length_mat_x + length_mat_y and \
                        (next_x, next_y-1) != (prev_x, prev_y):
                    queue.append([next_x, next_y-1, dis+1, next_x, next_y])
                if next_y+1 < length_mat_y and \
                        dis < length_mat_x + length_mat_y and \
                        (next_x, next_y+1) != (prev_x, prev_y):
                    queue.append([next_x, next_y+1, dis+1, next_x, next_y])

            return max_dis

        for i in range(length_mat_x):
            answer.append([])
            for j in range(length_mat_y):
                value = mat[i][j]
                if value == 0:
                    answer[i].append(0)
                else:  # == 1
                    answer[i].append(bfs(i, j))

        return answer


print(Solution().updateMatrix(mat=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == [
      [0, 0, 0], [0, 1, 0], [0, 0, 0]])
print(Solution().updateMatrix(mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]]) == [
      [0, 0, 0], [0, 1, 0], [1, 2, 1]])
