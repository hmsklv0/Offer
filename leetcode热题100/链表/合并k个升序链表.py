# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        # 歪路子
        # 将所有的节点放入列表，借助列表的排序功能进行排序，而后将节点进行组合
        if lists is None:
            return None

        list_nodes = []

        for head_node in lists:
            if head_node is None:
                continue

            node = head_node
            while node is not None:
                list_nodes.append(node)
                node = node.next
        # 排序
        list_nodes.sort()

        dummy_node = ListNode()
        node = dummy_node

        for item_node in list_nodes:
            node.next = item_node
            node = node.next
        if len(list_nodes) != 0:
            item_node.next = None
        return dummy_node.next

    def mergeTwoLists(self, h1: ListNode, h2: ListNode):
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
        node.next = h1 if h1 is not None else h2
        return dummy_node.next

    def mergeKLists2(self, lists: list[ListNode]) -> ListNode:

        # 自顶向下进行分治，先分治，再合并
        def recuv(recuv_lists: list[ListNode]) -> ListNode:
            # 结束条件
            m = len(recuv_lists)
            if m == 0:
                return None
            elif m == 1:
                # 无需合并直接返回
                return recuv_lists[0]
            # 分割
            mid = m // 2
            left_list = recuv_lists[:mid]

            right_list = recuv_lists[mid:]

            # 合并
            return self.mergeTwoLists(recuv(left_list), recuv(right_list))
        return recuv(lists)
