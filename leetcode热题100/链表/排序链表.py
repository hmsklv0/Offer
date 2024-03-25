# 题解 https://leetcode.cn/problems/sort-list/solutions/13728/sort-list-gui-bing-pai-xu-lian-biao-by-jyd/?envType=study-plan-v2&envId=top-100-liked
# 归并排序，（自顶向下）先利用快慢指针分割，而后合并两个左右两边链表，递归调用
# 归并排序，（自底向上）
# 奇淫技巧：利用python list自带的排序功能，用list将所有节点进行添加，而后排序，再按照顺序进行连接
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        # 1 字典生成
        node = head
        node_dict = {}
        while node is not None:
            if node.val in node_dict:
                node_dict[node.val].append(node)
            else:
                node_dict[node.val] = [node]
            node = node.next

        # 2 生成有序数组
        nums_list = []
        for i in node_dict.keys():
            nums_list.append(i)

        nums_list.sort()

        # 3 根据有序数组生成有序链表
        dummy_node = ListNode()
        node = dummy_node.next
        for i in nums_list:
            i_list_nodes = node_dict[i]
            for item_node in i_list_nodes:
                node = item_node
                node = node.next
            last_i = i
        node.next = None
        return dummy_node.next

    def sortList2(self, head: ListNode) -> ListNode:
        # 思路改进，直接通过列表排序，不通过字典绕路
        node = head
        node_list = []
        if head is None:
            return None
        # 1 列表排序
        while node:
            node_list.append(node)
            node = node.next
        node_list.sort(key=lambda x: x.val)
        # 2 按排序列表进行节点重组
        dummy_node = ListNode()
        node = dummy_node
        for item_node in node_list:
            node.next = item_node
            node = node.next

        item_node.next = None
        return dummy_node.next


    def sortList3(self, head: ListNode) -> ListNode:
        # 归并排序自顶向下
        def recuv(head_node: ListNode):
            # 先拆分，再合并
            if head_node is None or head_node.next is None:
                return head_node
            # 利用快慢指针找到中线
            fast, slow = head_node.next, head_node
            while fast is not None and fast.next is not None:
                fast = fast.next.next
                slow = slow.next
            mid, slow.next = slow.next, None

            # 拆分
            left, right = recuv(head_node), recuv(mid)

            dummy_node = ListNode()
            node = dummy_node
            # 合并
            while left is not None and right is not None:
                if left.val > right.val:
                    # 注意不要忘记 right 和 left自己迭代
                    node.next = right
                    right = right.next
                else:
                    node.next = left
                    left = left.next
                node = node.next
            node.next = left if left is not None else right

            return dummy_node.next
        return recuv(head)

    def merge(self, h1: ListNode, h2: ListNode) -> ListNode:
        dummy_node = ListNode()
        node = dummy_node

        while h1 is not None and h2 is not None:
            if h1.val < h2.val:
                node.next = h1
                h1 = h1.next
            else:
                node.next = h2
                h2 = h2.next
            node = node.next

        if h1 is not None:
            node.next = h1
        else:
            node.next = h2
        return dummy_node.next

    def sortList4(self, head: ListNode) -> ListNode:
        # 归并排序 自底向上
        node = head
        length = 0
        # 统计长度
        while node is not None:
            length += 1
            node = node.next

        # 最外层循环, subLength * 2 循环
        dummy_node = ListNode()
        dummy_node.next = head

        subLength = 1
        while subLength < length:
            pre = dummy_node
            curr = dummy_node.next

            # 遍历 subLength 分层，逐个遍历 subLength 长度的左右小链表，将其排序合并
            while curr:
                # 寻找h1
                h1 = curr
                for i in range(1, subLength):
                    if curr.next is None:
                        break
                    curr = curr.next

                # 寻找h2
                h2 = curr.next
                curr.next = None
                curr = h2
                for i in range(1, subLength):
                    if curr is None or curr.next is None:
                        break
                    curr = curr.next

                # curr 前进1
                if curr is not None:
                    next = curr.next
                    curr.next = None
                    curr = next

                # h1 和 h2 归并
                merged = self.merge(h1, h2)
                pre.next = merged
                while pre.next is not None:
                    pre = pre.next

            subLength = subLength * 2

        return dummy_node.next