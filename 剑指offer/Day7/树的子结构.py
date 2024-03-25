# Definition for a binary tree node.
from 构造树 import Tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if B is None or A is None:
            return False

        def recur(a: TreeNode, b: TreeNode) -> bool:
            # 1 匹配当前节点，然后向下匹配
            if b is None:
                # 终止情况
                return True
            if a is None or b.val != a.val:
                return False
            else:
                # 2 符合条件，向下匹配
                if recur(a.left, b.left) and recur(a.right, b.right):
                    return True
        # 递归调用
        # 当前匹配，下一个轮左节点匹配 右节点匹配
        return recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

# A = [1, 2, 3]
# B = [3, 1]

# A = [1,2,3,4]
# B = [3]
A = [3,4,5,1,2]
B = [4, 1]

A_t = Tree(A)
B_t = Tree(B)

A_n = A_t.root
B_n = B_t.root

solution = Solution()
print(solution.isSubStructure(A_n, B_n))

