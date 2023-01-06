from collections import defaultdict, Counter
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        root_size = len(parents)

        dict_score_TO_count = defaultdict(int)

        dict_parent_TO_children = defaultdict(list)

        for index_parent, parent in enumerate(parents):
            dict_parent_TO_children[parent].append(index_parent)

        def createTree(node) -> TreeNode:
            children = dict_parent_TO_children.get(node)

            if children:
                list_tree = []
                for child in children:
                    tree_node = createTree(child)
                    list_tree.append(tree_node)

                return TreeNode(node, *list_tree)
            else:
                return TreeNode(node)

        root = createTree(0)

        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0

            size_left = dfs(root.left)
            size_right = dfs(root.right)

            remaining_node_count = root_size - size_left - size_right - 1

            score = max(remaining_node_count, 1) * \
                max(size_left, 1) * max(size_right, 1)

            dict_score_TO_count[score] += 1

            return size_left + size_right + 1

        dfs(root)

        return dict_score_TO_count[max(dict_score_TO_count.keys())]


# print(Solution().countHighestScoreNodes(parents=[-1, 2, 0, 2, 0]) == 3)
# print(Solution().countHighestScoreNodes(parents=[-1, 2, 0]) == 2)
print(Solution().countHighestScoreNodes(parents=[-1,3,3,5,7,6,0,0]) == 2)
