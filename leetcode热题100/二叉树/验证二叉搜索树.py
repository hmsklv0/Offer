# 题解 https://leetcode.cn/problems/validate-binary-search-tree/solutions/230256/yan-zheng-er-cha-sou-suo-shu-by-leetcode-solution/?envType=study-plan-v2&envId=top-100-liked
# 思路1 采用自顶向下的方法，将二叉搜索树节点的值给定范围
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 失败的方法，只能比较局部，不能比较全局
        # 采用递归的方式
        def recuv(node: Optional[TreeNode]):
            # 终止条件
            if node is None:
                return True
            # 左右子树都为二叉搜索树，继续判断
            if not recuv(node.left) or not recuv(node.right):
                return False
            if node.right is not None:
                if node.val > node.right.val:
                    return False
            if node.left is not None:
                if node.val < node.left.val:
                    return False

            return True

        return recuv(root)

    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        def recuv(node: Optional[TreeNode], lower=float('-inf'), upper=float('inf')) -> bool:
            # 终止条件
            if node is None:
                return True
            print(node.val)
            # 判断条件

            if not recuv(node.left, lower=lower, upper=node.val) or not recuv(node.right, upper=upper, lower=node.val):
                print(1, node.val)

                return False
            # 全局判断
            if node.val >= upper or node.val <= lower:
                print(2, node.val)

                return False
            # 局部判断
            if node.right is not None:

                if node.val > node.right.val:
                    print(3, node.val)

                    return False
            if node.left is not None:

                if node.val < node.left.val:
                    print(4, node.val)

                    return False
            return True

        return recuv(root)
