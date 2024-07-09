# 思路一，首先A先跑一次，然后记录所有的节点内存地址，遍历B进行对比
# https://leetcode.cn/problems/intersection-of-two-linked-lists/solutions/10774/tu-jie-xiang-jiao-lian-biao-by-user7208t/?envType=study-plan-v2&envId=top-100-liked
# 思路二，两者都走同样的路径，这样迟早会相遇
# 两者相加，然后从后往前看，如果相交，那么，必定尾部的一段是重合的，或者说是相同的
# pA:1->2->3->4->5->6->null->9->5->6->null
# pB:9->5->6->null->1->2->3->4->5->6->null

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        nodeA = headA
        nodeB = headB
        intersectVal = {}
        while True:
            if nodeA is None:
                break
            intersectVal[id(nodeA)] = 1
            nodeA = nodeA.next

        while True:
            if nodeB is None:
                break
            if id(nodeB) in intersectVal:
                return nodeB
            nodeB = nodeB.next
        return None

    def getIntersectionNode2(self, headA: ListNode, headB: ListNode):
        nodeA = headA
        nodeB = headB
        while nodeA is not nodeB:
            # None作为一个单独的一步，保证 n + m 后必定结束循环，因为nodeA nodeB均为None
            nodeA = headB if nodeA is None else nodeA.next
            nodeB = headA if nodeB is None else nodeB.next
        return nodeA
