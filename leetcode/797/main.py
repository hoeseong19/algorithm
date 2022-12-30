from typing import List
from collections import deque


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        answer = []

        dict_from_number_To_list_to_number = {}

        for from_number, list_to_number in enumerate(graph):
            dict_from_number_To_list_to_number[from_number] = list_to_number

        def dfs(start: int, end: int):
            queue = deque([[start]])

            while queue:
                path = queue.popleft()

                from_number = path[-1]

                if from_number == end:
                    answer.append(path)

                list_to_number = dict_from_number_To_list_to_number[from_number]

                for to_number in list_to_number:
                    tmp_path = path[::]
                    tmp_path.append(to_number)
                    queue.append(tmp_path)

        dfs(0, len(graph) - 1)

        return answer


print(Solution().allPathsSourceTarget(
    graph=[[1, 2], [3], [3], []]) == [[0, 1, 3], [0, 2, 3]])
print(Solution().allPathsSourceTarget(graph=[[4, 3, 1], [3, 2, 4], [3], [
      4], []]) == [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]])
