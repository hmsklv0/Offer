# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        element = []
        def recuv(node: Optional[TreeNode]):
            if node is None:
                return

            recuv(node.left)
            # 中序遍历
            element.append(node.val)
            recuv(node.right)
        recuv(root)
        return element[k-1]
