# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        res = []
        def recuv(root: TreeNode):
            if root is None:
                return
            recuv(root.left)
            res.append(root.val)
            recuv(root.right)
        recuv(root)
        return res

    def inorderTraversal_Iteration(self, root: TreeNode) -> list[int]:
        stack = []
        res = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right

        return res

