from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        hi, hj = height[i], height[j]
        max_area = min(hi, hj)*(j-i)

        while i != j:
            if hi < hj:
                i += 1
                hi = height[i]
            else:
                j -= 1
                hj = height[j]

            current_area = min(hi, hj) * (j - i)
            if current_area > max_area:
                max_area = current_area
        return max_area
