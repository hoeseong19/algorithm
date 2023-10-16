from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        else:
            answer = []
            answer.append(1)

            row = self.getRow(rowIndex - 1)

            for i in range(rowIndex - 1):
                answer.append(row[i] + row[i + 1])

            answer.append(1)

            return answer


print(Solution().getRow(rowIndex=3) == [1, 3, 3, 1])
print(Solution().getRow(rowIndex=0) == [1])
print(Solution().getRow(rowIndex=1) == [1, 1])
