# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_node = ListNode(0,head)
        fast, slow = head, dummy_node

        while fast is not None:
            if fast.val == val:
                slow.next = fast.next
                fast = fast.next
            fast = fast.next
            slow = slow.next
        return dummy_node.next

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_node = ListNode(0,head)
        node = dummy_node

        while node.next is not None:
            cur_node = node.next
            if cur_node.val == val:
                node.next = cur_node.next
            else:
                node = node.next
        return dummy_node.next