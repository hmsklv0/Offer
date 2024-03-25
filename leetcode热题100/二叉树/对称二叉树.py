from typing import Optional
from tool_Tree import Tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        left_node = []
        right_node = []

        def recuv1(node: Optional[TreeNode]):
            # 终止条件
            if node is None:
                left_node.append(node)
                return
            recuv1(node.left)
            recuv1(node.right)
            left_node.append(node)

        def recuv2(node: Optional[TreeNode]):
            # 终止条件
            if node is None:
                right_node.append(node)
                return
            recuv2(node.right)
            recuv2(node.left)
            right_node.append(node)

        recuv1(root.left)
        recuv2(root.right)
        l_len, r_len = len(left_node), len(right_node)

        if l_len != r_len:
            return False
        for i in range(l_len):
            if left_node[i] is None or right_node[i] is None:
                if left_node[i] is not right_node[i]:
                    return False
                else:
                    continue

            if left_node[i].val != right_node[i].val:
                return False
        return True


tree_list = [1, 2, 2, None, 3, None, 3]
tree = Tree(tree_list)
# print(tree.printTree())
a = Solution()
a.isSymmetric(tree.root)
