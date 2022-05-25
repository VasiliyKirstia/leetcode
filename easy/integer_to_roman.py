class Solution:
    alphabet = list(reversed([
        (1, 'I'),
        (4, 'IV'),
        (5, 'V'),
        (9, 'IX'),
        (10, 'X'),
        (40, 'XL'),
        (50, 'L'),
        (90, 'XC'),
        (100, 'C'),
        (400, 'CD'),
        (500, 'D'),
        (900, 'CM'),
        (1000, 'M'),
    ]))

    def intToRoman(self, num: int) -> str:
        result = ''

        while num > 0:
            for (value, sign) in self.alphabet:
                while num - value >= 0:
                    result += sign
                    num -= value
        return result


if __name__ == '__main__':
    s = Solution()
    for v in [3, 58, 1994]:
        print(s.intToRoman(v), v)
