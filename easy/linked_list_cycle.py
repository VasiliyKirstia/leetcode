from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        while True:
            if head.next is None:
                return False
            if head.val is None:
                return True

            head.val = None
            head = head.next


if __name__ == '__main__':
    s = Solution()
