from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2
        root = ListNode(None)
        current = root

        while p1 is not None or p2 is not None:
            if p1 is not None and p2 is not None:
                if p1.val <= p2.val:
                    node = ListNode(p1.val)
                    current.next = node
                    current = node
                    p1 = p1.next
                else:
                    node = ListNode(p2.val)
                    current.next = node
                    current = node
                    p2 = p2.next
            elif p1 is not None:
                node = ListNode(p1.val)
                current.next = node
                current = node
                p1 = p1.next
            elif p2 is not None:
                node = ListNode(p2.val)
                current.next = node
                current = node
                p2 = p2.next

        return root.next


if __name__ == '__main__':
    s = Solution()
    print(s.isValid('[{([][][][}](){})}]'))