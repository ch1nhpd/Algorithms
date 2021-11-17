

'''

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

'''

class Solution:
    def isMatch(s: str, p: str) -> bool:
        def dp(i,j):
            if j == len(p):
                return i==len(s)
            else:
                first_match = i<len(s) and (s[i] == p[j] or p[j] == '.')
                if j < len(p) - 1 and p[j+1] =='*':
                    #  Matches zero     or    more of the preceding element.
                    return dp(i, j + 2) or first_match and dp(i+1,j)
                else:
                    return first_match and dp(i+1,j+1)
        return dp(0,0)

print(Solution.isMatch('ab','.a'))