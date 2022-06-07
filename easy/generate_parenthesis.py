from typing import List


class Solution:
    def generate(self, s, n, op, cl, mem):
        if op == n and cl == n:
            mem.append(s)
            return

        if op < n:
            self.generate(s + '(', n, op + 1, cl, mem)

        if cl < op:
            self.generate(s + ')', n, op, cl + 1, mem)


    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.generate('', n, 0, 0, result)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(1))
    print(s.generateParenthesis(2))
    print(s.generateParenthesis(3))
    print(s.generateParenthesis(4))

