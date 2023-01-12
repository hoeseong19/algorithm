from collections import Counter, defaultdict
from typing import List


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        answer = [0 for _ in range(n)]

        list2_node = [[] for _ in range(n)]

        for from_node, to_node in edges:
            list2_node[from_node].append(to_node)
            list2_node[to_node].append(from_node)

        def dfs(prev, from_node):
            label = labels[from_node]
            label_counter = Counter(label)

            list_to_node = list2_node[from_node]

            for to_node in list_to_node:
                if to_node != prev:
                    label_counter += dfs(from_node, to_node)

            answer[from_node] = label_counter[label]

            return label_counter

        dfs(None, 0)

        return answer


print(Solution().countSubTrees(n=7, edges=[[0, 1], [0, 2], [1, 4], [
      1, 5], [2, 3], [2, 6]], labels="abaedcd") == [2, 1, 1, 1, 1, 1, 1])
print(Solution().countSubTrees(n=4, edges=[
      [0, 1], [1, 2], [0, 3]], labels="bbbb") == [4, 2, 1, 1])
print(Solution().countSubTrees(n=5, edges=[[0, 1], [0, 2], [
      1, 3], [0, 4]], labels="aabab") == [3, 2, 1, 1, 1])
