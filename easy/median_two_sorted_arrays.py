from typing import List
import math


class Solution:
    def m2(self, a, b):
        return (a + b)/2

    def m3(self, a, b, c):
        return a + b + c - max(a,b,c) - min(a, b, c)

    def m4(self, a, b, c, d):
        return 0.5 * (a+b+c+d - max(a,b,c,d) - min(a,b,c,d))

    def median(self, ar1, n, ar2, m) -> List[int]:
        print(ar1, n, ar2, m)

        if n == 1:
            if m == 1:
                return self.m2(ar1[0], ar2[0])
            elif m % 2 == 1:
                return self.m3(ar1[0], ar2[0], ar2[1])
            elif

            return ar1 + ar2

        m1 = ar1[len(ar1) // 2]
        m2 = ar2[len(ar2) // 2]

        if m1 == m2:
            return m1

        if m1 < m2:
            return self.median(ar1, ar2[:len(ar2) // 2 + len(ar2) % 2])
        return self.median(ar1[:len(ar1) // 2 + len(ar1) % 2], ar2)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m2 = self.median(nums1, nums2, len(nums2) + len(nums1))
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
