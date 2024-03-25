# https://leetcode.cn/problems/copy-list-with-random-pointer/solutions/889166/fu-zhi-dai-sui-ji-zhi-zhen-de-lian-biao-rblsf/?envType=study-plan-v2&envId=top-100-liked
# 官方题解：节点复制到原节点后面，然后开始
# 思路2：利用哈希表一一对应的原理，将原节点与新节点一一对应（第一次循环），在第二次循环时，对新节点的next和random进行补充
# 先把题目抄了，再根据每个题目抄对应的答案

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if head is None:
            return None
        node = head
        old_to_new = {}
        while node is not None:
            new_node = Node(node.val)
            old_to_new[id(node)] = new_node
            node = node.next

        node = head
        while node is not None:
            new_node = old_to_new[id(node)]

            if node.next is None:
                new_node.next = None
            else:
                new_node.next = old_to_new[id(node.next)]

            if node.random is None:
                new_node.random = None
            else:
                new_node.random = old_to_new[id(node.random)]

            node = node.next
        return old_to_new[id(head)]
