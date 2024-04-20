# https://leetcode.cn/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/solutions/2721724/jian-ji-xie-fa-pythonjavacjs-by-endlessc-3vri/?envType=daily-question&envId=2024-04-03
# 回溯类型
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        path = []
        res = []

        def recur(node: TreeNode, cur_target: TreeNode):
            if node is None:
                return

            if node is cur_target:
                res.append(path[:])
                return

            path.append(0)
            recur(node.left, cur_target)
            path.pop()
            path.append(1)
            recur(node.right, cur_target)
            path.pop()

        recur(original, target)
        node = cloned
        if len(res) >= 1:
            for i in res[0]:
                if i == 0:
                    node = node.left
                else:
                    node = node.right
        return node

    def getTargetCopy2(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        res = []

        def recur(original_node: TreeNode, cloned_node: TreeNode, cur_target: TreeNode):
            if original_node is None:
                return

            if original_node is cur_target:
                res.append(cloned_node)
                return

            recur(original_node.left, cloned_node.left, cur_target)
            recur(original_node.right, cloned_node.right, cur_target)

        recur(original, cloned, target)

        return res[0]
