# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        level = 0
        nums = []

        # 递归调用
        def helper(level, node: TreeNode, nums: list[list[int]]):
            if node is not None:
                # 如果没有当前层没有被创建，则创建一个
                if len(nums) < level + 1:
                    nums.append([])
                # 添加当前节点的值进数组
                nums[level].append(node.val)
                # 左节点
                if node.left is not None:
                    helper(level + 1, node.left, nums)
                # 右节点
                if node.right is not None:
                    helper(level + 1, node.right, nums)

        helper(level, root, nums)
        return nums

