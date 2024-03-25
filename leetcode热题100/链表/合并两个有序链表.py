# Definition for singly-linked list.
# 题解 https://leetcode.cn/problems/merge-two-sorted-lists/solutions/226408/he-bing-liang-ge-you-xu-lian-biao-by-leetcode-solu/?envType=study-plan-v2&envId=top-100-liked
# 思路1 迭代
# 思路2 递归

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # 优化方法包括初始化一个哑节点
        # 使用循环方法，逐个添加解决
        l1 = list1
        l2 = list2
        # 为空处理
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        # 1 确定链表头的位置
        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        node = head

        # 2 循环添加
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        # 3 尾部添加(同时处理当l1和l2同时为None的情况)
        if l1 is None:
            node.next = l2
        if l2 is None:
            node.next = l1
        return head

    def mergeTwoLists2(self, list1: ListNode, list2: ListNode) -> ListNode:
        # 递归方法解决
        # list1[0]+merge(list1[1:],list2)       list1[0]<list2[0]
        # list2[0]+merge(list1,list2[1:])       otherwise

        def merge(l1: ListNode, l2: ListNode) -> ListNode:
            # 两个if将所有为空的情况都处理完成
            if l1 is None:
                return l2
            if l2 is None:
                return l1

            if l1.val <= l2.val:
                node = l1
                node.next = merge(l1.next, l2)
            else:
                node = l2
                node.next = merge(l1, l2.next)

            return node

        return merge(list1, list2)