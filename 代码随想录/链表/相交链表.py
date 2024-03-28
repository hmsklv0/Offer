from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodeA = headA
        nodeB = headB

        while nodeA is not nodeB:
            # None作为一个单独的一步，保证 n + m 后必定结束循环，因为nodeA nodeB均为None
            # if 条件不能设置为 nodeA.next is None, 不然会导致死循环
            nodeA = headB if nodeA is None else nodeA.next
            nodeB = headA if nodeB is None else nodeB.next
        return nodeA
