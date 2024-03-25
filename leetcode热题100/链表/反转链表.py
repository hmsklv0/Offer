# 题解 https://leetcode.cn/problems/reverse-linked-list/solutions/2361282/206-fan-zhuan-lian-biao-shuang-zhi-zhen-r1jel/?envType=study-plan-v2&envId=top-100-liked
# 三种思路 栈（复制数组）、递归、循环
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        node_stack = []
        node = head
        while node is not None:
            node_stack.append(node)
            print(node.val)
            node = node.next
        node = node_stack.pop()
        res = node

        while node_stack:
            node.next = node_stack.pop()
            node = node.next
        node.next = None
        return res

    def reverseList2(self, head: ListNode) -> ListNode:
        # 使用递归
        def recur(node, pre):
            # 终止条件, 当 next 为空时，返回节点
            if node is None:
                return pre

            # res作为最后的节点，一直被返回
            res = recur(node.next, node)

            # 反转操作，将当前节点的next指向前一个节点
            node.next = pre
            return res

        return recur(head, None)

    def reverseList3(self, head: ListNode) -> ListNode:
        # 使用循环
        if head is None:
            return None
        node = head
        pre = None
        # 用 next 是因为不好返回 node,但其实可以返回 pre
        while node.next is not None:
            node.next, pre, node = pre, node, node.next
            # 完整写法如下，使用tmp暂存
            # tmp = node.next
            # node.next = pre
            # # 进入下一次循环
            # pre = node
            # node = tmp

        node.next = pre
        return node

    def reverseList4(self, head: ListNode) -> ListNode:

        if head is None:
            return None
        node = head
        pre = None
        while node is not None:
            node.next, pre, node = pre, node, node.next

        return pre
