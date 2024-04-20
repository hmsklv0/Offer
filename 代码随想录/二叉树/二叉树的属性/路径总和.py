# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        def recur(node: TreeNode, target: int) -> bool:
            if not node.left and not node.right and target == 0:
                return True
            elif not node.left and not node.right:
                return False

            if node.left is not None:
                if recur(node.left, target - node.left.val):
                    return True
            if node.right is not None:
                if recur(node.right, target - node.right.val):
                    return True
            return False

        return recur(root, targetSum - root.val)
