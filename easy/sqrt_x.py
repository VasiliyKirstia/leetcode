class Solution:
    def mySqrt(self, x: int) -> int:
        current_odd = 1
        root = 0
        while x >= current_odd:
            x -= current_odd
            root += 1
            current_odd += 2
        return root


if __name__ == '__main__':
    s = Solution()

    print(s.mySqrt(8))
    print(s.mySqrt(9))
    print(s.mySqrt(25))
    print(s.mySqrt(225**2))
    print(s.mySqrt(0))
    print(s.mySqrt(2**31 - 1 ))