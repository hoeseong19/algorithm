from collections import defaultdict
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        answer = 0

        dict_from_edge_TO_list_to_edge = defaultdict(list)

        for from_edge, to_edge in edges:
            dict_from_edge_TO_list_to_edge[from_edge].append(to_edge)
            dict_from_edge_TO_list_to_edge[to_edge].append(from_edge)

        def dfs(prev, index):
            list_to_edge = dict_from_edge_TO_list_to_edge.get(index)

            if list_to_edge is None:
                if hasApple[index]:
                    return 2
                else:
                    return 0
            else:
                sum_time = 0

                for to_edge in list_to_edge:
                    if prev != to_edge:
                        sum_time += dfs(index, to_edge)

                if sum_time > 0:
                    sum_time += 2
                else:
                    if hasApple[index]:
                        sum_time += 2

            return sum_time

        answer = dfs(None, 0)

        if answer > 0:
            answer -= 2

        return answer


print(Solution().minTime(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [
      2, 6]], hasApple=[False, False, True, False, True, True, False]) == 8)
print(Solution().minTime(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [
      2, 6]], hasApple=[False, False, True, False, False, True, False]) == 6)
print(Solution().minTime(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [
      2, 6]], hasApple=[False, False, False, False, False, False, False]) == 0)
print(Solution().minTime(n=4, edges=[[0, 1], [1, 2], [
      0, 3]], hasApple=[True, True, True, True]) == 6)
