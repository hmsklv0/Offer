# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        def cur(r: ListNode, l: ListNode) -> ListNode:
            if r is None and l is None:
                return None
            elif r is None:
                node = l
                node.next = cur(None, l.next)
            elif l is None:
                node = r
                node.next = cur(r.next, None)
            else:
                # 都不为空
                if r.val < l.val:
                    node = r
                    node.next = cur(r.next, l)
                else:
                    node = l
                    node.next = cur(r, l.next)

            return node

        # head = cur(l1, l2)
        return cur(l1, l2)


l1 = ListNode(1)
for i in [2, 4]:
    node1 = ListNode(i)
    l1.next = node1

l2 = ListNode(1)
for j in [3, 4]:
    node1 = ListNode(j)
    l2.next = node1
solution = Solution()

print(solution.mergeTwoLists(l1, l2).val)