from typing import List
from collections import Counter


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        answer = 0

        counter_tasks = Counter(tasks)

        for count_task in counter_tasks.values():
            if count_task < 2:
                answer = -1
                break
            else:
                answer += (count_task + 2) // 3

        return answer


print(Solution().minimumRounds(tasks=[2, 2, 3, 3, 2, 4, 4, 4, 4, 4]) == 4)
print(Solution().minimumRounds(tasks=[2, 3, 3]) == -1)
