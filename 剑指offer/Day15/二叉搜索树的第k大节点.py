# Definition for a binary tree node.
from 二叉树.构造树 import Tree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        count = 0
        result = 0
        def dfs(node: TreeNode):
            nonlocal count
            if node is None:
                return
            dfs(node.left)
            count += 1
            # print(node.val, count)

            dfs(node.right)
        def dfs2(node: TreeNode):
            nonlocal count
            nonlocal result
            nonlocal node_numbers
            if node is None:
                return
            dfs2(node.left)

            count += 1
            if count == node_numbers - k:
                result = node.val
                # return
            print(node.val, count)

            dfs2(node.right)

        dfs(root)
        node_numbers = count
        print(node_numbers)
        count = -1
        dfs2(root)

        return result

    def kthLargest2(self, root: TreeNode, k: int) -> int:
        count = 0
        result = 0
        def dfs(node : TreeNode):
            nonlocal count
            nonlocal result
            if node is None:
                return
            dfs(node.right)
            count += 1
            if count == k:
                result = node.val
                return
            dfs(node.left)
        dfs(root)
        return result


tree_list = [3, 1, 4, None, 2]
# tree_list = [5, 3, 6, 2, 4, None, None, 1, None]

tree = Tree(tree_list)
# print(tree.printTree())

solution = Solution()
print(solution.kthLargest2(tree.root, 1))
