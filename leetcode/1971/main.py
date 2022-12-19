from typing import List
from collections import deque, defaultdict


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        answer = False

        q_vertex = deque([source])

        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        while q_vertex:
            vertex = q_vertex.popleft()

            if vertex == destination:
                answer = True

                break

            while graph[vertex]:
                q_vertex.append(graph[vertex].pop())

        return answer


solution = Solution()


print(solution.validPath(n=3, edges=[
      [0, 1], [1, 2], [2, 0]], source=0, destination=2) == True)
print(solution.validPath(n=6, edges=[[0, 1], [0, 2], [3, 5], [
      5, 4], [4, 3]], source=0, destination=5) == False)
