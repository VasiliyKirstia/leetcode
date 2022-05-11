from typing import List


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        n_hops = 0
        size = len(nums)
        i = 1

        while i < size:
            if nums[i-1] < nums[i]:
                i += 1
            else:
                # print(i, nums[i-1], nums[i], nums[i+1])
                if i == 1 or i + 1 == size:
                    n_hops += 1
                    i += 1
                elif nums[i-1] < nums[i+1]:
                    n_hops += 1
                    i += 2
                elif nums[i-2] < nums[i]:
                    n_hops += 1
                    i += 1
                else:
                    return False
        return n_hops <= 1


if __name__ == '__main__':
    s = Solution()
    print(s.canBeIncreasing([1, 2, 10, 4, 7]))
    print(s.canBeIncreasing([1, 2, 1, 4, 7]))
    print(s.canBeIncreasing([10, 2, 3, 4, 7]))
    print(s.canBeIncreasing([1, 2, 10, 4, 1]))

