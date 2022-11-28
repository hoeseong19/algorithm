from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.answer = 0

        def dfs(root: Optional[TreeNode]):
            if root is None:
                return -1
            else:
                left = dfs(root.left)
                right = dfs(root.right)

                dist = left + right + 2

                self.answer = max(dist, self.answer)
                return max(left, right) + 1

        dfs(root)

        return self.answer


solution = Solution()


print(solution.diameterOfBinaryTree(root=TreeNode(
    1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))) == 3)
print(solution.diameterOfBinaryTree(
    root=TreeNode(1, TreeNode(2))) == 1)
