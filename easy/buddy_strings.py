class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) == 1:
            return False

        if len(s) != len(goal):
            return False

        n_unique = len(set(s))
        mismatch_idx = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                mismatch_idx.append(i)

        if (
            len(mismatch_idx) == 2
            and s[mismatch_idx[0]] == goal[mismatch_idx[1]]
            and s[mismatch_idx[1]] == goal[mismatch_idx[0]]
        ):
            return True

        if len(mismatch_idx) == 0 and n_unique < len(s):
            return True

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.buddyStrings('aa', 'aa'))
    print(s.buddyStrings('ab', 'ab'))
    print(s.buddyStrings('aabcda', 'aacbda'))
    print(s.buddyStrings('aabcda', 'aaccda'))
    print(s.buddyStrings('aabcda', 'baadca'))
    print(s.buddyStrings('ab', 'babbb'))


# https://leetcode.com/problems/buddy-strings/
