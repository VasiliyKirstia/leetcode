from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs:
            new_prefix = []
            for i in range(min(len(prefix), len(s))):
                if prefix[i] == s[i]:
                    new_prefix.append(s[i])
                else:
                    break
            prefix = ''.join(new_prefix)
        return prefix


if __name__ == '__main__':
    s = Solution()
    print('|', s.longestCommonPrefix(['safd', 'afd', 'afddf', 'afdffd']), '|')
