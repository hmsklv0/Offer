from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recuv(root: Optional[TreeNode]) -> Optional[TreeNode]:
            # 结束条件
            if root is None:
                return

            # 左右子树交换位置
            left = recuv(root.left)
            right = recuv(root.right)

            root.left = right
            root.right = left

            return root
        return recuv(root)
