# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
            以栈的形式记录节点，以逆序(pop)的形式重新构造反转链表
        """
        stack_node = []

        # 空链表处理
        if head is None:
            return None

        # 将节点按链表顺序压栈
        while head:
            stack_node.append(head)
            head = head.next

        # 将节点按链表逆序出栈
        head = stack_node.pop()
        return_head = head
        while stack_node:
            head.next = stack_node.pop()
            head = head.next
        # 终止条件为：栈为空，此时 head 指向最后一个节点，因此最后设置 head.next 指向为空
        head.next = None

        # 返回反转链表的首节点
        return return_head


class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        # 递归
        def recur(cur, pre):
            if not cur: return pre  # 终止条件
            res = recur(cur.next, cur)  # 递归后继节点
            cur.next = pre  # 修改节点引用指向
            return res  # 返回反转链表的头节点

        # 最后终止情况，cur为None，返回pre，回到上一级递归，这时，res为链表的尾节点
        # 同时，当前节点的 cur.next 指向前节点，返回尾巴节点（即：一直返回的都是同一个尾节点）
        return recur(head, None)  # 调用递归并返回


class Solution3:
    # 迭代
    def reverseList(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        # 将cur.next 指向 pre节点，并用tmp保存后续节点，进行从而进行迭代
        while cur:
            tmp = cur.next # 暂存后继节点 cur.next
            cur.next = pre # 修改 next 引用指向
            pre = cur      # pre 暂存 cur
            cur = tmp      # cur 访问下一节点
        return pre





def main():
    node_head = ListNode(1)
    node_index = node_head
    for i in range(2, 6):
        node = ListNode(i)
        node_index.next = node
        node_index = node_index.next
    solution = Solution()
    node = solution.reverseList(node_head)
    # 输出构造链表
    # node = node_head
    while node is not None:
        print(node.val)
        node = node.next


if __name__ == '__main__':
    main()
