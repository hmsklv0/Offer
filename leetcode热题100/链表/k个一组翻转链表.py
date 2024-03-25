# 官方题解https://leetcode.cn/problems/reverse-nodes-in-k-group/solutions/248591/k-ge-yi-zu-fan-zhuan-lian-biao-by-leetcode-solutio/?envType=study-plan-v2&envId=top-100-liked
# 好题解 https://leetcode.cn/problems/reverse-nodes-in-k-group/solutions/1992228/you-xie-cuo-liao-yi-ge-shi-pin-jiang-tou-plfs/?envType=study-plan-v2&envId=top-100-liked
# 通过构造哑节点和单次k翻转进行解决，难点在于细节处理
# 官方解法
# 每次循环k个节点，将头尾节点作为参数传递给 翻转函数
# 若不足则直接返回哑节点.next

# 自己解法：遍历得到总节点数，从而计算翻转次数

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        index = 0

        # 1 计算翻转次数
        node = head
        while node is not None:
            index += 1
            node = node.next

        count = index // k

        # 2 构造哑节点
        dummy_node = ListNode()
        dummy_node.next = head

        # 3 进行翻转
        count_node = dummy_node
        node = head
        tail_node = node

        for i in range(count):

            pre = None
            count_k = 0
            # k 个节点的链表翻转
            while count_k < k:
                count_k += 1
                node.next, pre, node = pre, node, node.next
            head_node = pre

            # 将翻转后的链表连接
            count_node.next = head_node
            count_node = tail_node
            # node 自动转换，因为在翻转的最后一步 node = node.next
            # node = node
            tail_node = node
        count_node.next = node

        return dummy_node.next
