# 官方题解 https://leetcode.cn/problems/swap-nodes-in-pairs/solutions/444474/liang-liang-jiao-huan-lian-biao-zhong-de-jie-di-91/?envType=study-plan-v2&envId=top-100-liked
# 思路1 迭代，构造哑节点迭代遍历
# 思路2 递归
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        # 构造哑巴节点作为起点
        dummy_node = ListNode()
        dummy_node.next = head

        pair_1 = dummy_node
        pair_2 = head.next

        while pair_1 is not None and pair_2 is not None:

            # 方法1 逐个交换
            # m_node = pair_1.next
            # # 1 将m_node 和 pair_2 指向的节点交换位置，即将m_node放到 pair_2 和 pair_2.next 中间
            # m_node.next = pair_2.next
            # pair_2.next = m_node
            # # 2 pair_2 接上原本 m_node 的位置
            # pair_1.next = pair_2
            #
            # # # 3 将交换后的 pair_2指向正确的位置
            # pair_2 = m_node

            # 方法2 简化处理
            pair_1.next.next, pair_2.next, pair_1.next = pair_2.next, pair_1.next, pair_2
            pair_2 = pair_2.next

            # 循环，处理边界情况 2 种情况，pair_2后 有一个节点或者没有节点
            if pair_2.next is None:
                break
            pair_1 = pair_2
            pair_2 = pair_2.next.next

        # 注意是返回哑节点的后续节点，而不是返回head
        return dummy_node.next

    def swapPairs2(self, head: ListNode) -> ListNode:

        def recuv(node: ListNode):
            if node is None or node.next is None:
                return node
            # 假设这是最后一层，将当前节点和后一个节点交换位置，不用管node的前一个节点
            tmp = node.next
            node.next = recuv(node.next.next)
            tmp.next = node

            return tmp

        return recuv(head)
