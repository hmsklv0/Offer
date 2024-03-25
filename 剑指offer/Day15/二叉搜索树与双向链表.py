"""
# Definition for a Node.

"""

from 二叉树.构造树 import Tree


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: Node) -> Node:
        if root is None:
            return None

        def dfs(node: Node) -> (Node, Node):
            if node.left is not None and node.right is None:
                # 只有左子树
                right_tail = node
                left_head, left_tail = dfs(node.left)

                # 双链表
                left_tail.right = node
                node.left = left_tail

                return left_head, right_tail
            elif node.left is None and node.right is not None:
                # 只有右子树
                left_head = node
                right_head, right_tail = dfs(node.right)

                # 双链表
                node.right = right_head
                right_head.left = node

                return left_head, right_tail

            elif node.right is None and node.left is None:
                # 如果当前节点没有左右子树，那么没有必要修改
                return node, node
            else:
                # 正常情况下，左右子树都有
                # 左边尾巴
                left_head, left_tail = dfs(node.left)
                # 右边尾巴
                right_head, right_tail = dfs(node.right)

                # 归并 left + node + right
                # 双链表 node.left
                node.left = left_tail
                left_tail.right = node
                # 双链表 node.right
                node.right = right_head
                right_head.left = node

                return left_head, right_tail

        head, tail = dfs(root)
        head.left = tail
        tail.right = head
        return head


tree_list = [4, 2, 5, 1, 3]
tree = Tree(tree_list)
print(tree.printTree())

solution = Solution()
nodex = solution.treeToDoublyList(tree.root)
for i in range(5):
    print(nodex.val)
    nodex = nodex.right
