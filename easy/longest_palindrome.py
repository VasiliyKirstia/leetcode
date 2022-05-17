class Solution:
    def longestPalindrome(self, s: str) -> str:
        value = s[0]
        global_max = 1
        len_s = len(s)

        for i in range(len_s):

            current_max = 1
            for j in range(1, min(i+1, len_s - i)):

                if s[i - j] == s[i + j]:
                    current_max += 2
                    if current_max > global_max:
                        global_max = current_max
                        value = s[i-j:i+j+1]
                else:
                    break

            current_max = 0
            for j in range(1, min(i+1, len_s - i + 1)):
                if s[i - j] == s[i + j - 1]:
                    current_max += 2
                    if current_max > global_max:
                        global_max = current_max
                        value = s[i-j:i+j]
                else:
                    break

        return value


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome('1233455432111'))
    print(s.longestPalindrome('f'))
    print(s.longestPalindrome('ff'))
    print(s.longestPalindrome('fe'))
    print(s.longestPalindrome('feeeeeeeeeeef'))