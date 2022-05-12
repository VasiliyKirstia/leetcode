from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while right - left > 1:
            half = (left + right) // 2
            if nums[half] < target:
                left = half
            elif target < nums[half]:
                right = half
            else:
                return half

        if target < nums[left] or nums[left] == target:
            return left
        if nums[right] == target:
            return right
        if nums[right] < target:
            return right + 1
        return right


if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1,2,3,4,5,6,7], 4))
    print(s.searchInsert([1,2,3,4,5,6,7], 15))
    print(s.searchInsert([1,2,3,4,5,6,7], -1))
    print(s.searchInsert([1,2,3,4,5,6,7], 1))
    print(s.searchInsert([1], 3))
    print(s.searchInsert([1], -1))
    print(s.searchInsert([1,3], 1))
