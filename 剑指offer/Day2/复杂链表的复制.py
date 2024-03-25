"""
# Definition for a Node.

"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic = {}
        node = head
        # 01 创建对应的新节点
        if node is None:
            return None
        while node:
            dic[node] = Node(node.val)
            node = node.next

        # 02 根据原有节点的信息，将新节点进行串接
        for old_node, new_node in dic.items():
            if old_node.next is not None:
                new_node.next = dic[old_node.next]
            if old_node.random is not None:
                new_node.random = dic[old_node.random]
        return dic[head]

class Solution2:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return
        cur = head
        # 1. 复制各节点，并构建拼接链表
        while cur:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        # 2. 构建各新节点的 random 指向
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 3. 拆分两链表
        cur = res = head.next
        pre = head
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None # 单独处理原链表尾节点
        return res      # 返回新链表头节点


