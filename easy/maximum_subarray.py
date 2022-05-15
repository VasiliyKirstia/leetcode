
class Solution:
    def maxSubArray(self, a):

        current_max = float('-inf')
        current_sum = 0

        for i in range(len(a)):
            current_sum += a[i]
            if current_max < current_sum:
                current_max = current_sum

            if current_sum < 0:
                current_sum = 0
        return current_max


if __name__ == '__main__':
    s = Solution()

    print(s.maxSubArray([-1,1,2,5,-15,1,2,3]))
    print(s.maxSubArray([-2, -3, 4, -1, -2, 1, 5, -3]))
    print(s.maxSubArray([-1, -1, -2, -5, 15, -1, -2]))
