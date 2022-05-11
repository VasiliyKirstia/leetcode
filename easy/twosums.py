from typing import List
from operator import itemgetter

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = zip(nums, range(len(nums)))
        data = sorted(data, key=itemgetter(0))

        head = 0
        tail = len(nums) - 1

        while head < tail:
            result = data[head][0] + data[tail][0]
            if result == target:
                return [data[head][1], data[tail][1]]
            elif result < target:
                head += 1
            else:
                tail -= 1


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([9,4,5,6,7,8], 15))