class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# n 为偶数: return the second middle node.
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


# n 为偶数: return the first middle node.
class Solution2:
    def middleNode(self, head: ListNode) -> ListNode:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# n 为奇数，始终指向队列中线
