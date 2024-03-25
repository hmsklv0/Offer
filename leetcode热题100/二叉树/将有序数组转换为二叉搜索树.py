from typing import Optional
from tool_Tree import Tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        if nums is None:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        # 找到中线返回 TreeNode
        def recuv(val, l_list, r_list) -> Optional[TreeNode]:
            print(val)
            node = TreeNode(val)

            # 终止条件
            l_len = len(l_list)
            r_len = len(r_list)
            if l_len == 0 and r_len == 0:
                return node
            elif l_len == 0:
                # 只看 r_list
                print("r_list", r_list)

                r_mid = r_len // 2
                node.right = recuv(r_list[r_mid], r_list[:r_mid], r_list[r_mid + 1:])

            elif r_len == 0:
                # 只看 l_list
                print("l_list", l_list)

                l_mid = l_len // 2
                node.left = recuv(l_list[l_mid], l_list[:l_mid], l_list[l_mid + 1:])

            else:
                # r_list， l_list
                print(l_list, r_list)
                l_mid = l_len // 2
                r_mid = r_len // 2
                node.left = recuv(l_list[l_mid], l_list[:l_mid], l_list[l_mid + 1:])
                node.right = recuv(r_list[r_mid], r_list[:r_mid], r_list[r_mid + 1:])

            return node

        length = len(nums)
        mid = length // 2
        root = recuv(nums[mid], nums[:mid], nums[mid + 1:])
        return root


list1 = [-10, -3, 0, 5, 9]

# print(tree.printTree())
a = Solution()
node = a.sortedArrayToBST(list1)
tree = Tree([])
tree.root = node
print(node.val)

tree.printTree()
