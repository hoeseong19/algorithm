from collections import deque
from typing import Deque, List, Optional, Tuple

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer: List[List[int]] = []

        q_node: Deque[Tuple[Optional[TreeNode], int]] = deque([(root, 0)])

        while q_node:
            node = q_node.popleft()

            if node[0] is not None:
                if len(answer) <= node[1]:
                    answer.append([])

                if node[1] % 2 == 0:
                    answer[node[1]].append(node[0].val)
                else:
                    answer[node[1]].insert(0, node[0].val)

                q_node.append((node[0].left, node[1] + 1))
                q_node.append((node[0].right, node[1] + 1))

        return answer


print(Solution().zigzagLevelOrder(root=TreeNode(3, TreeNode(9, None, None),
      TreeNode(20, TreeNode(15), TreeNode(7)))) == [[3], [20, 9], [15, 7]])
print(Solution().zigzagLevelOrder(root=TreeNode(1)) == [[1]])
print(Solution().zigzagLevelOrder(root=None) == [])
