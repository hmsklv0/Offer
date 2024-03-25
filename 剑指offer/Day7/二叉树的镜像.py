# Definition for a binary tree node.
from 构造树 import Tree

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        def recur(node: TreeNode):
            if node is None:
                # 终止条件
                return
            else:
                # 1 交换左右子节点
                node.right, node.left = node.left, node.right
                # 2 调用递归函数，继续交换，直至终止条件
                recur(node.left)
                recur(node.right)
        recur(root)
        return root

