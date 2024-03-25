# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        # 定义一个栈
        list_num = []
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        #  利用栈先进后出的概念
        while stack:
            list_num.append(stack.pop())
        return list_num

    def reversePrint2(self, head: ListNode) -> List[int]:
        # 定义一个栈
        list_num = []
        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        return list_num[::-1]