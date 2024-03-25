# Definition for a binary tree node.

from tool_Tree import Tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        flag = 0
        result = []
        layer_nodes = [root]

        while layer_nodes:
            next_layer = []
            if not flag:
                # print(layer_nodes)
                result.append([j.val for j in layer_nodes])
            else:
                result.append([layer_nodes[-j].val for j in range(1, len(layer_nodes) + 1)])
            print("layer_nodes \t", layer_nodes)
            print("result\t\t\t", result)
            flag ^= 1
            for node in layer_nodes:
                if node.left is not None:
                    next_layer.append(node.left)
                if node.right is not None:
                    next_layer.append(node.right)
            print("next_layer\t\t", next_layer)

            layer_nodes = next_layer
        return result


root = [3, 9, 20, None, None, 15, 7]
tree = Tree(root)
a = Solution()
print(a.zigzagLevelOrder(tree.root))
