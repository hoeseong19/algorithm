from leetcode.utils.tree_node import TreeNode
from typing import Optional


class Solution:
    answer = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            self.answer = True

        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return -1

            else:
                degree_left = dfs(root.left)
                degree_right = dfs(root.right)
                if abs(degree_left - degree_right) > 1:
                    self.answer = False
                return max(degree_left, degree_right) + 1

        dfs(root)

        return self.answer


solution = Solution()
print(solution.isBalanced(TreeNode(3, TreeNode(9, None, None),
      TreeNode(20, TreeNode(15), TreeNode(7)))) == True)
print(solution.isBalanced(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(
    4), TreeNode(4)), TreeNode(3)), TreeNode(2, None, None))) == False)
print(solution.isBalanced(None) == True)
print(solution.isBalanced(TreeNode(1, None, TreeNode(2, None, TreeNode(3)))) == False)
print(solution.isBalanced(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(
    4), None), None), TreeNode(2, None, TreeNode(3, None, TreeNode(4))))) == False)
