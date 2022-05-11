from typing import List


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
            elif current > second_max and current != first_max:
                third_max = second_max
                second_max = current
            elif second_max is not None and third_max is not None and current > third_max and current != third_max:
                third_max = current

        print([first_max, second_max, third_max])

        if third_max is not None:
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

# https://leetcode.com/problems/third-maximum-number/
