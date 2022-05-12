from typing import List
from dataclasses import dataclass


@dataclass
class CombinedData:
    max_value: int
    max_value_idx: int
    all_data: List[int]
    data_len: int


class Solution:
    def split_combine(self, data):
        if len(data) <= 1:
            return data

        left = self.split_combine(data[:len(data)//2])
        right = self.split_combine(data[len(data)//2:])

        return self.merge(
            CombinedData(left[0], 0, left, 1) if left else None,
            CombinedData(right[0], 0, right, 1) if right else None,
        )

    def merge(self, left: CombinedData, right: CombinedData):
        if left is None or right is None:
            return left or right

        if left.data_len == 1 and right.data_len == 1:
            sum_ = left.max_value + right.max_value
            if sum_ >= max(left.max_value, right.max_value):
                return CombinedData(sum_, 0, [sum_], 1)
            else:
                if left.max_value > right.max_value:
                    return CombinedData(
                        left.max_value,
                        0,
                        [left.max_value, right.max_value],
                        2
                    )
                else:
                    return CombinedData(
                        right.max_value,
                        1,
                        [left.max_value, right.max_value],
                        2
                    )
        else:
            max_combined = sum(left.all_data[left.max_value_idx:] + right.all_data[:right.max_value_idx+1])
            if max_combined >= max(right.max_value, left.max_value):
                return CombinedData(
                    max_combined,
                    left.max_value_idx,
                    left.all_data[:left.max_value_idx] + [max_combined] + right.all_data[right.max_value_idx+1:],
                    left.max_value_idx + right.data_len - right.max_value_idx,
                )
            else:
                CombinedData(
                    max_combined,
                    left.max_value_idx,
                    left.all_data[:left.max_value_idx] + [max_combined] + right.all_data[right.max_value_idx + 1:],
                    left.max_value_idx + right.data_len - right.max_value_idx,
                )


        if left + right > left and left + right > right:
            return [left + right]
        return

    def maxSubArray(self, nums: List[int]) -> int:



if __name__ == '__main__':
    pass