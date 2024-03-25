from typing import Optional
from tool_Tree import Tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []
        node_list = []

        def recuv(node: Optional[TreeNode], layer):
            if node is None:
                return None
            if len(node_list) < layer:
                node_list.append(node)

            recuv(node.right, layer + 1)
            recuv(node.left, layer + 1)
        recuv(root, 1)
        return [node.val for node in node_list]


tree_list = [1, 2, 3, None, 5, None, 4]
tree = Tree(tree_list)
a = Solution()
print(a.rightSideView(tree.root))
