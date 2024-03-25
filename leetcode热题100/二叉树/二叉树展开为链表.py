from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node_list = []

        def recuv(node: TreeNode):
            if node is None:
                return

            node_list.append(node)
            recuv(node.left)
            recuv(node.right)


        recuv(root)
        dummy_node = TreeNode()
        node = dummy_node
        for node_item in node_list:
            node.right = node_item
            node = node.right
            node.left = None
        node.right = None

        return dummy_node.right
