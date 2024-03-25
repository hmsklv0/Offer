# https://programmercarl.com/0707.%E8%AE%BE%E8%AE%A1%E9%93%BE%E8%A1%A8.html#%E6%80%9D%E8%B7%AF
# 代码思路
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.dummy_node = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index + 1 > self.size:

            return -1
        node = self.dummy_node
        while index >= 0:
            node = node.next
            index -= 1
        print(node.val)
        return node.val

    def addAtHead(self, val: int) -> None:
        tmp_node = ListNode(val)
        if self.dummy_node.next is None:
            # 链表为空时 处理
            self.dummy_node.next = tmp_node
        else:
            tmp_node.next = self.dummy_node.next
            self.dummy_node.next = tmp_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        tmp_node = ListNode(val)
        head = self.dummy_node
        while head.next is not None:
            head = head.next
        head.next = tmp_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        # 注意 addAtIndex时有特殊情况，因此改为 index > self.size
        if index < 0 or index > self.size:
            return
        tmp_node = ListNode(val)
        node = self.dummy_node
        while index - 1 >= 0:
            node = node.next
            index -= 1
        tmp_node.next = node.next
        node.next = tmp_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index + 1 > self.size:
            print("deleteAtIndex out of index")

            return
        node = self.dummy_node
        while index - 1 >= 0:
            node = node.next
            index -= 1
        if node.next is not None:
            tmp_node = node.next
            del tmp_node
            node.next = node.next.next
        else:
            node.next = None

        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
