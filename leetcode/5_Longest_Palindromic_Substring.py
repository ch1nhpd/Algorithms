class Solution:
    def expand(s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - 1) - (left + 1) + 1

    def longestPalindrome(s: str) -> str:
        start = end = 0
        for i in range(0, len(s) - 1):
            len1 = Solution.expand(s, i, i)
            len2 = Solution.expand(s, i, i + 1)
            l = len1 if len1 > len2 else len2
            if l >= (end - start + 1):
                end = i + l // 2
                start = end + 1 - l
        return s[start:end + 1]


s = "babad"

print(Solution.longestPalindrome(s))
