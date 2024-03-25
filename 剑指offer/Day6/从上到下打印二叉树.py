# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> list[int]:
        # 使用队列完成一棵二叉树的打印，从队列弹出当前节点时，添加其左右子树节点
        queue = []
        queue.append(root)

        # 记录弹出队列的值
        return_list = []

        while len(queue) != 0:
            # 从队列弹出，添加其左右子节点
            node = queue.pop(0)

            if node is not None:
                return_list.append(node.val)
                leftnode = node.left
                rightnode = node.right
                # 如果左右子节点不为空，则添加进队列
                if leftnode is not None:
                    queue.append(leftnode)
                if rightnode is not None:
                    queue.append(rightnode)
            else:
                # node 为空
                break
        return return_list


