from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for number in nums:
            if number == val:
                pass
            else:
                nums[i] = number
                i += 1
        return i


if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([1, 2, 10, 4, 7], 1))
    print(s.removeElement([1, 2, 1, 4, 7], 1))
    print(s.removeElement([10, 2, 3, 4, 7], 7))
    print(s.removeElement([1, 2, 10, 4, 1], 10))
    print(s.removeElement([1], 1))
    print(s.removeElement([], 1))
