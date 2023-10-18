from collections import deque
from typing import List


class Solution:
    INDEX_PREV_COURCE = 0
    INDEX_NEXT_COURCE = 1

    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        answer = 0

        list_degree: List[int] = []
        list_min_time: List[int] = []
        list2_next_course: List[List[int]] = []

        for _ in range(n):
            list_degree.append(0)
            list_min_time.append(0)
            list2_next_course.append([])

        for relation in relations:
            list_degree[relation[self.INDEX_NEXT_COURCE] - 1] += 1
            list2_next_course[relation[self.INDEX_PREV_COURCE] - 1].append(relation[self.INDEX_NEXT_COURCE] - 1)

        q = deque([i for i in range(n) if list_degree[i] == 0])

        while q:
            course = q.popleft()

            list_min_time[course] += time[course]

            for next_course in list2_next_course[course]:
                list_degree[next_course] -= 1
                list_min_time[next_course] = max(list_min_time[next_course], list_min_time[course])

                if list_degree[next_course] == 0:
                    q.append(next_course)

        answer = max(list_min_time)

        return answer


print(Solution().minimumTime(n=3, relations=[[1, 3], [2, 3]], time=[3, 2, 5]) == 8)
print(Solution().minimumTime(n=5, relations=[[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], time=[1, 2, 3, 4, 5]) == 12)
