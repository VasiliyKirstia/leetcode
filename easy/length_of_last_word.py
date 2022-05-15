class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        idx = len(s)
        length = 0
        while idx > 0:
            idx -= 1
            if s[idx] == ' ':
                if length == 0:
                    continue
                return length
            else:
                length += 1
        return length


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord('   dfdfdf  d    '))
    print(s.lengthOfLastWord('   dfdfdf  d rtrt'))
    print(s.lengthOfLastWord('  '))
    print(s.lengthOfLastWord('  d    '))
    print(s.lengthOfLastWord('sdsd'))
    print(s.lengthOfLastWord('sdsdsdsd   '))