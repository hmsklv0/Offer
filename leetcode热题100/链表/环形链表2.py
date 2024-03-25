# 题解 https://leetcode.cn/problems/linked-list-cycle-ii/?envType=study-plan-v2&envId=top-100-liked
# 思路一: 使用集合较为简单
# 思路二: 使用快慢指针构造第一次相遇(总结点数为 a + b，慢指针的路径为 s)
# 思路二: 快指针路径 f = 2s
# 思路二: 同样也有 f = s + nb(在环上追上慢指针，即多跑n个环)
# 思路二: 可得 s = nb
# 思路二: 为什么构造第二次相遇呢？因为 当慢指针走到 a + nb 时, 刚好走到入环的位置
# 思路二: 如何走 a 的距离呢，构造一个新的指针，同时和慢指针一起走，走a的距离后，刚好在入环位置相遇
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 使用集合实现（字典也可以）
        node = head
        node_set = set()
        while node is not None:
            if id(node) in node_set:
                return node
            node_set.add(id(node))
            node = node.next
        return None

    def detectCycle2(self, head: ListNode) -> ListNode:
        # 构造快慢指针
        fast = head
        slow = head

        # 第一次相遇
        while True:
            if fast is None or fast.next is None:
                return None
            fast = fast.next.next
            slow = slow.next

            if fast is slow:
                print(fast.val, slow.val)
                break
        # 第二次相遇
        ptr = head
        while ptr != slow:
            print(ptr.val, slow.val)
            ptr, slow = ptr.next, slow.next
        return slow
