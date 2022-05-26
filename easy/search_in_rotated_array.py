from typing import List


class Solution:
    def get_index(self, nums, target, l, r):
        if l == r:
            if nums[l] == target:
                return l
            else:
                return -1
        if r - l == 1:
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            else:
                return -1

        i = (l+r)//2
        if nums[l] <= nums[i-1]:
            if nums[l] <= target <= nums[i-1]:
                return self.get_index(nums, target, l, i)
            else:
                return self.get_index(nums, target, i, r)
        else:
            if nums[i] <= target <= nums[r]:
                return self.get_index(nums, target, i, r)
            else:
                return self.get_index(nums, target, l, i)

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1

        return self.get_index(nums, target, 0, n - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.search([4,5,6,7,0,1,2], 0))
