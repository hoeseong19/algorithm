from collections import deque


class Solution:
    def __init__(self, row:int, col:int):
        self.row = row
        self.col = col

        self.maze = []

    def make_maze(self, row_str: str):
        row = []
        for c in row_str.strip():
            row.append(int(c))

        self.maze.append(row)

    def solve(self):
        answer = 0

        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]
        d = 4

        def bfs():
            self.maze[0][0] = 0

            q = deque([[0, 0, 1]])

            steps = 0

            while q:
                x, y, cur_step = q.popleft()

                # 목적지 도착?
                if (x, y) == (self.row-1, self.col-1):
                    steps = cur_step
                    break

                for i in range(d):
                    # 다음 위치
                    nx, ny = x + dx[i], y + dy[i]

                    # 범위를 벗어나지 않고 방문하지 않은 길
                    if (0 <= nx < self.row)\
                        and (0 <= ny < self.col)\
                        and self.maze[nx][ny] == 1:

                        # 중복이 생기는 걸 방지하기 위해 미리 방문여부를 설정
                        self.maze[nx][ny] = 0

                        q.append([nx, ny, cur_step+1])

            return steps

        answer = bfs()

        return answer

row, col = map(int, input().split(' '))

solution = Solution(row, col)

for _ in range(row):
    solution.make_maze(input())

print(solution.solve())
