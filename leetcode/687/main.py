from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    longest_univalue_path = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        answer = 0

        def dfs(root: Optional[TreeNode], parent):
            if root is None:
                return 0
            else:
                node = root.val

                longest_univalue_path__left = dfs(root.left, node)
                longest_univalue_path__right = dfs(root.right, node)

                self.longest_univalue_path = max(
                    self.longest_univalue_path, longest_univalue_path__left + longest_univalue_path__right)

                if node == parent:
                    longest_univalue_path__left += 1
                    longest_univalue_path__right += 1

                    return max(longest_univalue_path__left, longest_univalue_path__right)
                else:
                    return 0

        dfs(root, None)

        answer = self.longest_univalue_path

        return answer


print(Solution().longestUnivaluePath(root=TreeNode(5, TreeNode(
    4, TreeNode(1), TreeNode(1)), TreeNode(5, None, TreeNode(5)))) == 2)
print(Solution().longestUnivaluePath(root=TreeNode(1, TreeNode(
    4, TreeNode(4), TreeNode(4)), TreeNode(5, None, TreeNode(5)))) == 2)
