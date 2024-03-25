# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        stack_key = -1
        result_node = ListNode(0)

        def cur(node: ListNode):
            nonlocal stack_key
            nonlocal result_node
            if node is not None:
                cur(node.next)
            stack_key = stack_key + 1
            if stack_key == k:
                result_node = node
        cur(head)
        return result_node