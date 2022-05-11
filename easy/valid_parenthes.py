class Solution:
    allowed_parentheses = ['()', '[]', '{}']

    def isValid(self, s: str) -> bool:
        while True:
            previous_len = len(s)
            for pattern in self.allowed_parentheses:
                i = s.find(pattern)
                if i > -1:
                    s = s[:i]+s[i+2:]

            if len(s) == 0:
                return True
            if previous_len == len(s):
                return False


if __name__ == '__main__':
    s = Solution()
    print(s.isValid('[{([][][][}](){})}]'))
