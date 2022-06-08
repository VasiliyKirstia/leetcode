from typing import List
from functools import lru_cache


# class Solution:
#     @lru_cache
#     def get_max_cost(self, boxes):
#         if len(boxes) == 0:
#             return 0
#
#         max_cost = 0
#         j = i = 0
#         while i < len(boxes):
#             if boxes[i] != boxes[j]:
#                 cost = (i - j)**2
#                 rest_cost = self.get_max_cost(boxes[:j] + boxes[i:])
#                 if cost + rest_cost > max_cost:
#                     max_cost = cost + rest_cost
#                 j = i
#             i += 1
#
#         cost = (i - j) ** 2
#         rest_cost = self.get_max_cost(boxes[:j])
#         if cost + rest_cost > max_cost:
#             max_cost = cost + rest_cost
#
#         return max_cost
#
#     def removeBoxes(self, boxes: List[int]) -> int:
#         return self.get_max_cost(tuple(boxes))


class Solution:
    # A three dimensional DP is needed
    # Explanation: two dimensional DP is not suitable because once pop out contiguous subarray,
    #          elements outside the deleted subarray enters into the calculation
    # On the other hand, one should notice that elements outside the subarray matters only if
    #         there are other copies of the left end outside.
    # Example:
    # [1,3,2,2,2,3,4,3,1]
    # if we pop out the 2s, the 3 at index 1 enters the equation
    # if the given array changes to [7,5,2,2,2,3,4,3,1], then all the boxes on the
    #            left does not matter! One can define subproblems as in regular DP!
    # That's why the solutions in the forum all incur an extra k boxes on the left, because
    #             they are specifying the numbers that matters
    # In this problem, top-down is DFS + memo approach is more appropriate, as one does not
    #                   necessarily need to calculate all the i, j, k pairs

    def dfs(self, left, right, prev):
        if left > right:  # Stop the iteration when exhausting the array
            return 0
        elif (left, right, prev) in self.memo:
            return self.memo[(left, right, prev)]
        else:
            # If the front of the array is repeating
            # Example: [2,2,2,2,1]
            # Rather than calculating dfs(0,4,0) then dfs(1,4,1)... we just need dfs(3,4,3)
            shift = 0
            while left < right and self.boxes[left] == self.boxes[left + 1]:
                shift += 1
                left += 1
                prev += 1
            # DP
            # Two options:
            # 1. Remove the first one and all the ones before, get (k+1)*(k+1), together with everything after it
            # 2. Keep the first one and the boxes before it, try to remove the first (k+1) together with
            #     any identical boxes in the subarray.
            result = (prev + 1) * (prev + 1) + self.dfs(left + 1, right, 0)
            for i in range(left + 1, right + 1, 1):
                if self.boxes[i] == self.boxes[left]:
                    result = max(result, self.dfs(left + 1, i - 1, 0) + self.dfs(i, right, prev + 1))
            for i in range(0, shift + 1, 1):
                if (left - i, right, prev - i) not in self.memo:
                    self.memo[(left - i, right, prev - i)] = result
            return result

    def removeBoxes(self, boxes: List[int]) -> int:
        self.memo = {}
        self.boxes = boxes
        return self.dfs(0, len(boxes) - 1, 0)

if __name__ == '__main__':
    s = Solution()
    print(s.removeBoxes([1,1,2,1,1]))

#https://leetcode.com/problems/remove-boxes/