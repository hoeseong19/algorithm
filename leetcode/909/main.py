from collections import deque
from typing import List


class Solution:
    MAX_NUMBER_IN_6_SIDED_DIE = 6
    NOT_SNAKES_AND_LADDERS = -1

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        answer = -1

        q_board = deque([])

        for index, row in enumerate(board[::-1]):
            if index % 2 == 0:
                q_board.extend(row[::])
            else:
                q_board.extend(row[::-1])

        length_board = len(q_board)

        set_next_index = set()
        q_next = deque([[0, 0]])

        while q_next:
            cur_index, move = q_next.popleft()

            if cur_index == length_board - 1:
                answer = move
                break

            for i in range(1, self.MAX_NUMBER_IN_6_SIDED_DIE + 1):
                next_index = min(cur_index + i, length_board-1)
                next = q_board[next_index]

                if next != self.NOT_SNAKES_AND_LADDERS:
                    next_index = next-1

                if next_index not in set_next_index:
                    q_next.append([next_index, move+1])
                    set_next_index.add(next_index)

        return answer


print(Solution().snakesAndLadders(board=[[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -
      1, -1, -1, -1], [-1, 35, -1, -1, 13, -1], [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]) == 4)
print(Solution().snakesAndLadders(board=[[-1, -1], [-1, 3]]) == 1)
print(Solution().snakesAndLadders(
    board=[[1, 1, -1], [1, 1, 1], [-1, 1, 1]]) == -1)
