# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        path = [root.val]
        res = []

        def recur(node: TreeNode, cur_path: List[int], target: int):
            if not node.left and not node.right and target == 0:
                res.append(path[:])
                return
            elif not node.left and not node.right:
                return

            if node.left is not None:
                path.append(node.left.val)
                recur(node.left, path, target - node.left.val)
                path.pop()
            if node.right is not None:
                path.append(node.right.val)
                recur(node.right, path, target - node.right.val)
                path.pop()
        recur(root, path, targetSum-root.val)
        return res
