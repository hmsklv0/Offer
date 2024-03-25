# 思路1 递归
# 思路2 栈，循环


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 递归
        def recuv(node: Optional[TreeNode]):
            if node is None:
                return 0
            curr_layer = max(recuv(node.left), recuv(node.right)) + 1
            return curr_layer
        return recuv(root)


