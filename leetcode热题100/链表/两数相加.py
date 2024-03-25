# Definition for singly-linked list.
# 题解 https://leetcode.cn/problems/add-two-numbers/solutions/435246/liang-shu-xiang-jia-by-leetcode-solution/?envType=study-plan-v2&envId=top-100-liked
# 借助新链表存储

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 利用新创建的链表存储

        sum_head = ListNode()
        node = sum_head
        add = 0
        while l1 is not None and l2 is not None:
            # 进位处理
            node.val = (l1.val + l2.val + add) % 10
            add = (l1.val + l2.val + add) // 10

            if l1.next is None or l2.next is None:
                tail_node = node

            l1 = l1.next
            l2 = l2.next
            node.next = ListNode()
            node = node.next

        # 如果当前数据未曾比较完成
        if l1 is None and l2 is not None:
            while l2 is not None:
                node.val = (l2.val + add) % 10
                add = (l2.val + add) // 10
                if l2.next is None:
                    tail_node = node
                node.next = ListNode()
                node = node.next
                l2 = l2.next

        elif l2 is None and l1 is not None:
            while l1 is not None:
                node.val = (l1.val + add) % 10
                add = (l1.val + add) // 10
                if l1.next is None:
                    tail_node = node
                node.next = ListNode()
                node = node.next
                l1 = l1.next
        else:
            # l1 is None and l2 is None
            # tail_node.next = None
            pass
        if add != 0:
            # 若add未曾结束，则当前节点不需要删去
            node.val = add
        else:
            tail_node.next = None
        return sum_head

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 代码优化
        head, tail = None, None
        add = 0

        while l1 is not None or l2 is not None:
            l1_val = 0 if l1 is None else l1.val
            l2_val = 0 if l2 is None else l2.val
            # 进位处理 % 和 //
            sum = l1_val + l2_val + add

            if head is None:
                head = tail = ListNode(sum % 10)
            else:
                # 让 tail 始终指向 有数值的节点
                tail.next = ListNode(sum % 10)
                tail = tail.next
            add = sum // 10
            if l1 is not None:

                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        # 处理最后的进位
        if add > 0:
            tail.next = ListNode(add)
        return head
