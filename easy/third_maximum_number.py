from typing import List
import math


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max = float('-inf')
        second_max = None
        third_max = None

        for current in nums:
            if current > first_max:
                third_max = second_max
                second_max = first_max
                first_max = current
            elif current != first_max and (second_max is None or current > second_max):
                third_max = second_max
                second_max = current
            elif current != first_max and current != second_max and (third_max is None or current > third_max):
                third_max = current

        if third_max is not None and math.isfinite(third_max):
            return third_max
        return first_max


if __name__ == '__main__':
    s = Solution()
    print(s.thirdMax([1, 2, 10, 4, 7]))
    print(s.thirdMax([1, 2, 1, 4, 7]))
    print(s.thirdMax([10, 2, 3, 4, 7]))
    print(s.thirdMax([1, 2, 10, 4, 1]))
    print(s.thirdMax([1, 1, 1, 2, 3]))
    print(s.thirdMax([1, 1, 1, 2, 3,3]))
    print(s.thirdMax([1, 1, 1, 2]))
    print(s.thirdMax([1]))

# https://leetcode.com/problems/third-maximum-number/
