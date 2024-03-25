# Definition for singly-linked list.
# 官方题解 https://leetcode.cn/problems/palindrome-linked-list/solutions/457059/hui-wen-lian-biao-by-leetcode-solution/?envType=study-plan-v2&envId=top-100-liked
# 使用快慢指针和翻转链表做到空间复杂度O(1)

import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return False
        deque = collections.deque()

        node = head
        while node.next is not None:
            deque.append(node)
            node = node.next
        deque.append(node)
        tail = node
        while deque:
            if len(deque) == 1:
                break
            if deque.popleft().val != deque.pop().val:
                return False
        return True

    def isPalindrome2(self, head: ListNode) -> bool:
        self.front_pointer = head

        def recur(current_node):
            if current_node is not None:
                # 1 深入递归
                if not recur(current_node.next):
                    return False

                # 2 递归执行语句，使第一个元素和最后一个元素相向而行，进而进行判断
                if current_node.val != self.front_pointer.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recur(head)

    def isPalindrome3(self, head: ListNode) -> bool:
        def isPalindrome(self, head: ListNode) -> bool:
            if head is None or head.next is None:
                return True
            fast, slow = head, head

            # 1 利用快慢指针找到中间位置()
            while fast is not None and fast.next is not None:
                fast = fast.next.next
                if fast is not None and fast.next is not None:
                    slow = slow.next

            # 2 开始翻转链表
            start_reverse_node = slow.next
            node = start_reverse_node
            pre = None
            while node.next is not None:
                node.next, pre, node = pre, node, node.next
            node.next = pre

            # 3 链表对比
            tail = node
            start = head
            while tail is not None:
                if tail.val != start.val:
                    return False
                tail = tail.next
                start = start.next

            # 4 再次翻转链表
            pre = None
            while node.next is not None:
                node.next, pre, node = pre, node, node.next
            node.next = pre

            node = head
            while node is not None:
                print(node.val)
                node = node.next
            # 不用重新连接
            # slow.next = node
            return True
