from typing import Optional


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) < 1:
            return 0

        # if len(needle) == len(haystack):
        #     return 0 if haystack == needle else -1

        if len(needle) > len(haystack):
            return -1

        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i
        else:
            return -1


if __name__ == '__main__':
    s = Solution()
    print(s.strStr('c', 'cv'))