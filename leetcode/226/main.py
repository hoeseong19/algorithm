from typing import Optional


class TreeNode:  # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root: Optional[TreeNode]):
            if root:
                root.left, root.right = root.right, root.left
                dfs(root.left)
                dfs(root.right)

        dfs(root)

        return root


print(Solution().invertTree(root=TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(
    3)), TreeNode(7, TreeNode(6), TreeNode(9)))) == [TreeNode(4, TreeNode(7, TreeNode(9), TreeNode(6)), TreeNode(2, TreeNode(3), TreeNode(1)))])
print(Solution().invertTree(root=TreeNode(
    2, TreeNode(1), TreeNode(3))) == [TreeNode(2, TreeNode(3), TreeNode(1))])
print(Solution().invertTree(root=TreeNode()) == TreeNode())
