class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        str_start = 0
        vocabulary = set()

        for i in range(len(s)):
            if s[i] in vocabulary:
                # move two pointers and use set to check previous string (also remove redundand data from set and update current max substring)

