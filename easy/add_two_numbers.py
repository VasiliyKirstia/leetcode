from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(val=None)
        prev = None
        tail = head
        memory = 0

        while l1 is not None or l2 is not None:
            if l1 is not None:
                memory += l1.val
                l1 = l1.next

            if l2 is not None:
                memory += l2.val
                l2 = l2.next

            tail.val = memory % 10
            tail.next = ListNode(val=None)
            prev = tail
            tail = tail.next

            memory = memory // 10

        if memory > 0:
            tail.val = memory
        else:
            prev.next = None

        return head
