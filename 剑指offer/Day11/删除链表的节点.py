# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        append = ListNode(0)
        append.next = head

        node = append

        while node.next:
            if node.next.val == val:
                node.next = node.next.next
                break
            node = node.next
        return append.next
