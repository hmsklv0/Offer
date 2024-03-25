# Definition for a binary tree node.
from 构造树 import Tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        nums = []

        def recur(level, node: TreeNode):
            if level == len(nums):
                nums.append([])
            if node is None:
                # 终止条件
                nums[level].append(None)
            else:
                nums[level].append(node.val)
                recur(level + 1, node.left)
                recur(level + 1, node.right)
        recur(0, root)
        nums.pop()
        if len(nums) == 1:
            return True
        # print(nums)
        for i in range(1, len(nums)):
            list_1 = nums[i]
            result = 0
            for j in range(int(len(nums[i]) / 2)):
                if type(list_1[j]) == type(list_1[-(j+1)]) and list_1[j] is not None:
                    result += list_1[j] ^ list_1[-(j + 1)]
                elif type(list_1[j]) == type(list_1[-(j+1)]) and list_1[j] is None:
                    continue
                else:
                    return False

                # print(result)
            if result != 0:
                return False

        return True


list_A = [1, 2, 2, 3, 4, 4, 3]
Tree_A = Tree(list_A)
root_A = Tree_A.root

solution = Solution()
print(solution.isSymmetric(root_A))

