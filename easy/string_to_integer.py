class Solution:
    lower_bound = -2147483648
    upper_bound = 2147483647

    def read_int(self, s: str) -> (int, str):
        sign = None
        number = None

        for c in s:
            print(c, "'")
            if number is None and sign is None:
                if c == ' ':
                    pass
                elif c in '+-':
                    sign = c
                elif c in list('0123456789'):
                    number = c
                else:
                    return '', None
            else:
                print(number, f'"{c}"')
                if c in list('0123456789'):
                    number += c
                else:
                    return number or '', sign
        return number or '', sign

    def myAtoi(self, s: str) -> int:
        numb, sign = self.read_int(s)
        numb = numb.lstrip('0')

        if numb == '':
            return 0

        if len(numb) > 10:
            return self.lower_bound if sign == '-' else self.upper_bound

        converted = -int(numb) if sign == '-' else int(numb)

        if self.lower_bound <= converted <= self.upper_bound:
            return converted
        elif converted < self.lower_bound:
            return self.lower_bound
        else:
            return self.upper_bound


if __name__ == '__main__':
    s = Solution()

    for t in ["42",
    "   -42",
    "4193 with words",
    "---- 45",
    "+-23432",
    "0002147483648",
    "1112147483647",
    "-1112147483647",
    "   +   434"]:
        print(s.myAtoi(t))