# 官方题解 https://leetcode.cn/problems/remove-nth-node-from-end-of-list/solutions/450350/shan-chu-lian-biao-de-dao-shu-di-nge-jie-dian-b-61/?envType=study-plan-v2&envId=top-100-liked
# 思路：栈和递归的思路，双指针的思路
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 利用递归写法，从栈底+1找到倒数第n个节点
        self.index = 0

        def recuv(node: ListNode):
            # 返回当前节点，index == n时，返回下一个节点
            if node is None:
                return None
            node.next = recuv(node.next)
            self.index += 1
            if self.index == n:
                return node.next
            return node

        return recuv(head)

    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        # 利用双指针
        # 快指针先走 n 步
        # 然后快慢指针一起走
        # 因为总共为 a 个节点，这样一起走 a - n 步 刚好指向时，
        # 慢指针刚好指向倒数第 n 个节点的前一个节点
        index = 0
        dummy_node = ListNode()
        dummy_node.next = head
        fast, slow = head, dummy_node

        while index < n:
            index += 1
            fast = fast.next

        # 快指针 每个节点都遍历了一次，因此最后快指针走了 a -n 步
        while fast is not None:
            fast = fast.next
            slow = slow.next
        # 处理一个哑巴节点，便于慢指针指向前一个节点，从而快速删除节点
        if slow.next is not None:
            slow.next = slow.next.next
        return dummy_node.next

    def removeNthFromEnd3(self, head: ListNode, n: int) -> ListNode:

        dummy_node = ListNode(0, head)
        slow, fast = dummy_node, dummy_node
        i = 0
        # 让 fast 先走 n 步，这样就可以保证后面 slow 少走 n 步， 因为是从哑节点开始算起，因此假设总共由 a 个节点，后面slow总共走 a - n步，到达第 a -n 个节点
        # 即倒数第n个节点的前一个节点，然后删去这个节点
        while i < n:
            fast = fast.next
            i += 1

        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy_node.next
