from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 前序遍历
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def recur(node: TreeNode):
            if node is None:
                return
            res.append(node.val)
            recur(node.left)
            recur(node.right)

        recur(root)
        return res

    # 中序遍历
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def recur(node: TreeNode):
            if node is None:
                return
            recur(node.left)
            res.append(node.val)
            recur(node.right)

        recur(root)
        return res

    # 后序遍历
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def recur(node: TreeNode):
            if node is None:
                return

            recur(node.left)
            recur(node.right)
            res.append(node.val)

        recur(root)
        return res
