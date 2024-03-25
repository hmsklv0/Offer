from typing import Optional
from tool_Tree import Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        def recuv(pre_list, ino_list):
            if len(pre_list) == 0:
                return None
            if len(pre_list) == 1:
                return TreeNode(pre_list[0])
            node_val = pre_list[0]
            mid = ino_list.index(node_val)

            left = ino_list[:mid]
            right = ino_list[mid + 1:]
            print(node_val)

            print(left, right)
            print()

            node = TreeNode(node_val)

            node.left = recuv(pre_list[1:1 + len(left)], left)
            node.right = recuv(pre_list[1 + len(left):], right)
            return node

        return recuv(preorder, inorder)


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

a = Solution()

b = Tree([])
node1 = a.buildTree(preorder, inorder)
print(node1.val)
b.root = node1
print(b.printTree())

