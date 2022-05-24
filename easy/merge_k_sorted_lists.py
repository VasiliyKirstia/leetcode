from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge(self, l, r):
        if l.val > r.val:
            head = r
            r = r.next
        else:
            head = l
            l = l.next

        merged = head

        while l is not None or r is not None:
            if l is None:
                head.next = r
                head = r
                r = r.next

            elif r is None:
                head.next = l
                head = l
                l = l.next

            elif l.val < r.val:
                head.next = l
                head = l
                l = l.next
            else:
                head.next = r
                head = r
                r = r.next

        return merged

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        l = self.mergeKLists(lists[:len(lists)//2])
        r = self.mergeKLists(lists[len(lists)//2:])

        if l is None and r is None:
            return None
        if l is None:
            return r
        if r is None:
            return l

        return self.merge(l, r)


if __name__ == '__main__':
    s = Solution()

    print(s.mergeKLists([[1,2,3,4,5], [2,4,5,7,8], [4,6,8,9,12,56]]))
