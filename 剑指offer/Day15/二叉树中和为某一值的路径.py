from 二叉树.构造树 import Tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> list[list[int]]:
        result = []
        one_path = []

        def dfs(node: TreeNode, left_target: int):
            # 终止条件
            if node is None:
                return

            one_path.append(node.val)
            # 是否满足条件
            left_target -= node.val
            if left_target != 0:
                dfs(node.left, left_target)
                dfs(node.right, left_target)
            elif left_target == 0 and node.right is None and node.left is None:
                result.append(one_path.copy())
            else:
                # left_target < 0
                # and ( (node.right is not None) or (node.left is not None) )
                #
                # 这条路已经走不通了
                dfs(node.left, left_target)
                dfs(node.right, left_target)
                # pass
            one_path.pop()

        dfs(root, target)
        return result


# tree_list = [3, 9, 20, None, None, 15, 7]
# tree_list = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None,None, 5, 1]
# tree_list = [-2, None, -3]
tree_list = [1, -2, -3, 1, 3, -2, None, -1, None]
tree = Tree(tree_list)
print(tree.printTree())

solution = Solution()
print(solution.pathSum(tree.root, -1))
# [5,4,8,11,None,13,4,7,2,None,None,5,1]
