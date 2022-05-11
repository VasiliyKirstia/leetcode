from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current = 0

        if len(nums) > 1:
            for i in range(1, len(nums)):
                if nums[current] != nums[i]:
                    current += 1
                    nums[current] = nums[i]

        return current + 1


if __name__ == '__main__':
    s = Solution()
    l=[1,1,1,1,2,3,3,3,4,5,6,6]
    print(s.removeDuplicates(l), l)
