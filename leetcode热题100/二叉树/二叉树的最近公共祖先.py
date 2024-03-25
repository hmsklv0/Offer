from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path = []
        path_p = []
        path_q = []

        def cur(node: TreeNode):
            if node is None:
                return

            path.append(node)
            if node is p:
                path_p.extend(path)
            if node is q:
                path_q.extend(path)

            cur(node.left)
            cur(node.right)

            path.pop()

            return

        cur(root)

        ret = 0
        for i in range(len(path_q)):
            if path_p[i] is not path_q[i]:
                ret = i - 1
                break
        return path[ret]
