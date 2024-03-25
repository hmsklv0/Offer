from typing import Optional
from tool_Tree import Tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_sum = 0

        def recuv(node: Optional[TreeNode]):
            nonlocal max_sum
            if node is None:
                return 0
            left_depth, right_depth = recuv(node.left), recuv(node.right)
            depth = max(left_depth, right_depth) + 1
            tmp_sum = left_depth + right_depth
            max_sum = max(max_sum, tmp_sum)
            return depth

        recuv(root)
        return max_sum


tree_list = [1, 2, 3, 4, 5]
tree = Tree(tree_list)
# print(tree.printTree())
a = Solution()

print(a.diameterOfBinaryTree(tree.root))