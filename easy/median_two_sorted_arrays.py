from typing import List
import math


class Solution:
    def median(self, ar1, ar2) -> List[int]:
        print(ar1, ar2)

        if len(ar1) == 1 and len(ar2) == 1:
            return ar1 + ar2

        m1 = ar1[len(ar1) // 2]
        m2 = ar2[len(ar2) // 2]

        if m1 == m2:
            return m1

        if m1 < m2:
            return self.median(ar1, ar2[:len(ar2) // 2 + len(ar2) % 2])
        return self.median(ar1[:len(ar1) // 2 + len(ar1) % 2], ar2)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m1, m2 = self.median(nums1, nums2)
        if m1 == m2:
            return m1

        if len(nums1) == len(nums2):
            return 0.5 * (m1 + m2)

        if len(nums1) < len(nums2):
            return m2

        return m1



if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1,1,1,1,1], [2,2,2,2,2,2]))
    print(s.findMedianSortedArrays([0, 1, 3, 5], [1.5, 2.5]))
