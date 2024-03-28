# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)
        node = head
        pre = dummy_node
        while node is not None and node.next is not None:
            next_node = node.next.next
            # node 和 node.next 交换位置
            pre.next = node.next  
            node.next.next = node
            node.next = next_node

            pre = node

        return dummy_node.next

    def swapPairs2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recur(cur_node):
            if cur_node is None or cur_node.next is None:
                return cur_node
            # 待翻转的两个node分别是pre和cur
            pre = cur_node
            node = cur_node.next
            next_node = cur_node.next.next

            node.next = pre  # 交换
            pre.next = recur(next_node)  # 将以 next_node 为 head 的后续链表两两交换

            return node

        return recur(head)
