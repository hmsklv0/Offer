class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree:
    def __init__(self, listTree: list[int]):
        self.root = None
        self.status = 'null'
        self.level = 0
        if len(listTree) == 0:
            self.root = None
        else:
            self.root = self.createTree(listTree, 0)

    def createTree(self, listTree: list[int], i):
        # 结束条件
        # 1. 节点的索引超出树
        # 2. 当前节点在list中对应的位置为空 None
        if i >= len(listTree) or listTree[i] is None:
            return None
        else:
            # 主体创建树
            # 1. 创建当前节点
            # 2. 递归创建其左右子节点
            node = TreeNode(listTree[i])
            node.left = self.createTree(listTree, 2 * i + 1)
            node.right = self.createTree(listTree, 2 * i + 2)
            return node

    def printTree(self) -> list[list[int]]:
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

        helper(level, self.root, nums)
        return nums

#
# tree_list = [3, 9, 20, None, None, 15, 7]
# tree = tool_Tree(tree_list)
# print(tree.printTree())
