from collections import defaultdict, deque
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        answer = []

        dict_num_TO_visited = {}

        dict_num_TO_count = defaultdict(int)
        graph = defaultdict(list)

        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)

            dict_num_TO_visited[u] = False
            dict_num_TO_visited[v] = False

            dict_num_TO_count[u] += 1
            dict_num_TO_count[v] += 1

        start = None
        for k, v in dict_num_TO_count.items():
            if v == 1:
                start = k
                break
        q = deque([start])
        dict_num_TO_visited[start] = True
        answer.append(start)

        while q:
            next_num = q.popleft()

            for num in graph[next_num]:
                if dict_num_TO_visited[num]:
                    continue

                q.append(num)
                dict_num_TO_visited[num] = True
                answer.append(num)

        return answer


print(Solution().restoreArray(adjacentPairs=[[2, 1], [3, 4], [3, 2]]) == [1, 2, 3, 4])
print(Solution().restoreArray(adjacentPairs=[[4, -2], [1, 4], [-3, 1]]) == [-2, 4, 1, -3])
print(Solution().restoreArray(adjacentPairs=[[100000, -100000]]) == [100000, -100000])
