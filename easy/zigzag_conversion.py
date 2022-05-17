class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = []

        for j in range(numRows):
            i = 0
            while i*2*(numRows-1) + j < len(s):
                rows.append(s[i*2*(numRows-1) + j])
                if j not in (0, numRows - 1):
                    if (i+1)*2*(numRows-1) - j < len(s):
                        rows.append(s[(i+1)*2*(numRows-1) - j])
                i += 1

        return ''.join(rows)


if __name__ == '__main__':
    s = Solution()
    print(s.convert('PAYPALISHIRING', 4))
    print(s.convert('ASDSFSF', 1))
    print(s.convert('abcd', 3))
    print(s.convert('ab', 3))
    print(s.convert('abc', 3))
