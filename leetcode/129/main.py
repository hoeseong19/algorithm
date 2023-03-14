from typing import Optional


class TreeNode:  # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    answer = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(root: Optional[TreeNode], prev='0'):
            if root is None:
                self.answer += int(prev)
            else:
                if (root.left is not None) and (root.right is not None):
                    dfs(root.left, prev + str(root.val))
                    dfs(root.right, prev + str(root.val))
                elif root.left is not None:
                    dfs(root.left, prev + str(root.val))
                elif root.right is not None:
                    dfs(root.right, prev + str(root.val))
                else:
                    self.answer += int(prev + str(root.val))

        dfs(root)

        return self.answer


print(Solution().sumNumbers(root=TreeNode(1, TreeNode(2), TreeNode(3))) == 25)
print(Solution().sumNumbers(root=TreeNode(4, TreeNode(
    9, TreeNode(5), TreeNode(1)), TreeNode(0))) == 1026)
