from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def recuv(node: Optional[TreeNode]) -> int:
            nonlocal max_sum
            if node is None:
                return 0

            ret_l = max(recuv(node.left), 0)
            ret_r = max(recuv(node.right), 0)

            node_val = node.val
            max_sum = max(max_sum, node_val + ret_l + ret_r)

            return node_val + max(ret_l, ret_r)

        recuv(root)
        return max_sum