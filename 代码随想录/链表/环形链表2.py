from typing import Optional


class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_set = set()
        node = head
        while node is not None:
            if id(node) in node_set:
                return node
            node_set.add(id(node))
            node = node.next
        return None

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head

        # 第一次相遇
        while True:
            if fast is None or fast.next is None:
                # 无环的情况
                return None
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                break

        # 有环则，寻找入环点
        start = head
        while start is not slow:
            start = start.next
            slow = slow.next

        return start
