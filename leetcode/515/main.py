from collections import defaultdict
from typing import DefaultDict, Optional, List


class TreeNode:  # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        answer = 0

        def minInt():
            return pow(-2, 31)

        dict_level_TO_max: DefaultDict[int, int] = defaultdict(minInt)

        def dfs(root: Optional[TreeNode], level: int):
            if root is None:
                return

            dict_level_TO_max[level] = max(dict_level_TO_max[level], root.val)

            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)

        answer = list(dict_level_TO_max.values())

        return answer


print(
    Solution().largestValues(root=TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))) == [1, 3, 9]
)
print(Solution().largestValues(root=TreeNode(1, TreeNode(2), TreeNode(3))) == [1, 3])
