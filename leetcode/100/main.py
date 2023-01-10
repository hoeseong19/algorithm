from typing import List, Optional

from leetcode.utils.tree_node import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        answer = False

        list_p_tree_node = []
        list_q_tree_node = []

        def dfs(root: Optional[TreeNode], list_tree_node: List[Optional[int]]):
            if root is None:
                list_tree_node.append(None)
            else:
                list_tree_node.append(root.val)
                dfs(root.left, list_tree_node)
                dfs(root.right, list_tree_node)

        dfs(p, list_p_tree_node)
        dfs(q, list_q_tree_node)

        answer = list_p_tree_node == list_q_tree_node

        return answer


print(Solution().isSameTree(p=TreeNode(
    *[1, TreeNode(2), TreeNode(3)]), q=TreeNode(*[1, TreeNode(2), TreeNode(3)])) == True)
print(Solution().isSameTree(p=TreeNode(
    *[1, TreeNode(2)]), q=TreeNode(*[1, None, TreeNode(2)])) == False)
print(Solution().isSameTree(p=TreeNode(
    *[1, TreeNode(2), TreeNode(1)]), q=TreeNode(*[1, TreeNode(1), TreeNode(2)])) == False)
