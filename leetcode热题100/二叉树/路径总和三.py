import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        pre = collections.defaultdict(int)

        def recuv(node: TreeNode, curr):
            if node is None:
                return 0
            # 递增前缀和
            curr += node.val

            # 查询是否存在，并将当前前缀和存储
            ret = pre[curr - targetSum]
            pre[curr] += 1

            # 递归查询左右子树 是否存在ret
            ret += recuv(node.left, curr)
            ret += recuv(node.right, curr)

            return ret
        print(pre)
        return recuv(root, root.val)
