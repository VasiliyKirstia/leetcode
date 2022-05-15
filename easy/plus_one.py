from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last_idx = len(digits) - 1
        while last_idx >= 0:
            if digits[last_idx] == 9:
                digits[last_idx] = 0
                last_idx -= 1
            else:
                digits[last_idx] += 1
                return digits

        digits = [1] + digits

        return digits


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([1,9,9]))
    print(s.plusOne([1, 9, 8]))
    print(s.plusOne([9, 9, 9]))
    print(s.plusOne([9]))
    print(s.plusOne([0]))
    print(s.plusOne([5]))

