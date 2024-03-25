import collections
from typing import Optional
from tool_Tree import Tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []
        node_stack = collections.deque()
        node_stack.append(root)

        res = []

        # 循环层数为二叉树的深度，当当前层数没有节点时退出循环
        while node_stack:
            # 1 res 添加当前 node_stack 中（一层节点）的节点值
            res.append([])
            for i in node_stack:
                res[-1].append(i.val)


            # 2 node_stack 循环添加当前节点的左右子节点，为下一次循环做准备
            length = len(node_stack)
            index = 0
            while index < length:
                node = node_stack.popleft()
                if node.left is not None:
                    node_stack.append(node.left)
                if node.right is not None:
                    node_stack.append(node.right)
                index += 1

        return res






