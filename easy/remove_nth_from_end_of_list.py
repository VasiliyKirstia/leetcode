class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head

        previous = head
        i = 0
        current = head

        while current is not None:
            if i > n:
                previous = previous.next
            i += 1
            current = current.next

        if i <= n:
            return previous.next

        previous.next = previous.next.next

        return head
