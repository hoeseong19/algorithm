import sys
from collections import defaultdict, deque
from typing import DefaultDict, List


class Solution:
    def solve(self, start: int, graph: DefaultDict[int, List[int]]) -> None:
        list_dfs_visited = [False for _ in range(1_001)]
        list_dfs_visited_node = []
        list_bfs_visited = [False for _ in range(1_001)]
        list_bfs_visited_node = []

        def dfs(root: int):
            if list_dfs_visited[root]:
                return

            list_dfs_visited[root] = True
            list_dfs_visited_node.append(str(root))

            graph[root].sort()
            for child in graph[root]:
                dfs(child)

        def bfs(start: int):
            q = deque([start])

            list_bfs_visited[start] = True

            while q:
                cur = q.popleft()

                list_bfs_visited_node.append(str(cur))

                graph[cur].sort()
                for next in graph[cur]:
                    if list_bfs_visited[next]:
                        continue

                    list_bfs_visited[next] = True
                    q.append(next)

        dfs(start)
        print(" ".join(list_dfs_visited_node))
        bfs(start)
        print(" ".join(list_bfs_visited_node))

        return


nodes, edges, start = map(int, sys.stdin.readline().rstrip().split())
graph = defaultdict(list[int])
for _ in range(edges):
    node_1, node_2 = map(int, sys.stdin.readline().rstrip().split())
    graph[node_1].append(node_2)
    graph[node_2].append(node_1)
Solution().solve(start, graph)

with open("./baekjoon/1260/input.txt", "r") as f:
    n_cases = int(f.readline().rstrip())
    for _ in range(n_cases):
        nodes, edges, start = map(int, f.readline().rstrip().split(" "))
        graph = defaultdict(list[int])
        for _ in range(edges):
            node_1, node_2 = map(int, f.readline().rstrip().split(" "))
            graph[node_1].append(node_2)
            graph[node_2].append(node_1)
        Solution().solve(start, graph)
