class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        str_start = 0
        vocabulary = {}

        for i in range(len(s)):

            if s[i] in vocabulary:
                current_len = i - str_start

                previous_idx = vocabulary[s[i]]
                str_start = previous_idx + 1

                vocabulary = {c: k for k, c in enumerate(s[str_start:i + 1], start=str_start)}
            else:
                current_len = i - str_start + 1
                vocabulary[s[i]] = i

            if max_len < current_len:
                max_len = current_len

        return max_len


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring('abcdefabcdefg12'))
    print(s.lengthOfLongestSubstring('12312312312'))
