# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 利用 字典 求相同
        nodeA_dict = {}
        nodeB_dict = {}

        while headA is not None or headB is not None:
            if headA is None:
                # 在 B 链表中寻找
                nodeB_dict.get(headB, 1)
                if nodeA_dict.get(headB) == 1:
                    return headB
                else:
                    headB = headB.next
            elif headB is None:
                # 在 A 链表中寻找
                nodeA_dict.get(headA, 1)
                if nodeB_dict.get(headA) == 1:
                    return headA
                else:
                    headA = headA.next

            else:
                nodeA_dict.setdefault(headA, 1)
                nodeB_dict.setdefault(headB, 1)
                if nodeA_dict.get(headB) == 1:
                    return headB
                elif nodeB_dict.get(headA) == 1:
                    return headA
                else:
                    headA = headA.next
                    headB = headB.next
        return None


def printListNode(node: ListNode):
    while node:
        print(node.val, end='\t')
        node = node.next
    print()

def printListNodeID(node: ListNode):
    while node:
        print(id(node), end='\t')
        node = node.next
    print()

l1 = ListNode(4)
head1 = l1
for i in [1]:
    node1 = ListNode(i)
    l1.next = node1
    l1 = l1.next

l2 = ListNode(5)
head2 = l2
for j in [0, 1]:
    node1 = ListNode(j)
    l2.next = node1
    l2 = l2.next

node2 = ListNode(8)
l1.next = node2
l2.next = node2
for j in [4, 5]:
    node3 = ListNode(j)
    node2.next = node3
    node2 = node2.next

# printListNode(head1)
# printListNodeID(head1)
# printListNode(head2)
# printListNodeID(head2)
solution = Solution()
print(solution.getIntersectionNode(l1, l2).val)
