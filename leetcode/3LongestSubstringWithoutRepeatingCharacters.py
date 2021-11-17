'''
Given a string s, find the length of the longest substring without repeating characters.

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxx = 0
        A = []
        for i in s:
            try:
                index = A.index(i)
            except:
                index = -1
            A = A[index + 1:]
            A.append(i)
            tmp = len(A)
            if maxx < tmp:
                maxx = tmp
        return maxx
