# 官方题解 https://leetcode.cn/problems/linked-list-cycle/solutions/440042/huan-xing-lian-biao-by-leetcode-solution/?envType=study-plan-v2&envId=top-100-liked
# 题解 https://leetcode.cn/problems/linked-list-cycle/solutions/175734/yi-wen-gao-ding-chang-jian-de-lian-biao-wen-ti-h-2/?envType=study-plan-v2&envId=top-100-liked
# 思路：快慢指针能在2n时间内解决问题
# 进入环后，变成追及问题
# 2t- t = n + x(x为初始差值，n 为环值)
# 因此只要有环，快指针必能追上慢指针，从而相等，退出循环
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        node = head
        node_dict = set()
        while node is not None:
            if id(node) in node_dict:
                return True
            else:
                node_dict.add(id(node))
            node = node.next

        return False

    def hasCycle2(self, head: ListNode) -> bool:
        fast = head
        slow = head
        while fast is not None and fast.next is not None:

            fast = fast.next.next
            slow = slow.next
            # 放前面会导致初始值相同，从而返回true
            if fast is slow:
                return True
        return False
