from ast import List


# flag = 0
class Solution:
    def wordBreak(s, wordDict) :
        preFixList = ['']
        considered = set([])
        while len(preFixList) > 0:
            preFix = preFixList.pop(0)
            if preFix == s:
                return True

            for word in wordDict:
                subStr = preFix + word
                if subStr == s[:len(subStr)] and subStr not in considered:
                    preFixList = [subStr] + preFixList # add to head 
                    considered.add(subStr)

        return False           
            
# s = "leetcode"
# wordDict = ["leet","code"]       
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict=["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]     
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print(Solution.wordBreak(s=s,wordDict=wordDict))


