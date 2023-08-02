from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        pCounter = Counter(p)
        for i in range(len(s)-len(p)+1):
            currStr = s[i:i+len(p)]
            currStrCounter = Counter(currStr)
            if(currStrCounter == pCounter):
                ans = ans + [i]
        return(ans)

    
    def findAnagrams2(self, s: str, p: str) -> List[int]:

        l = 0
        r = len(p) - 1
        pDict = {}
        currDict = {}
        currWord = s[l:r+1]
        ans = []

        for currChar in p:
            pDict[currChar] = pDict.get(currChar, 0) + 1

        for currChar in currWord:
            currDict[currChar] = currDict.get(currChar, 0) + 1 

        while(r < len(s)):
            
            if(currDict == pDict):
                ans = ans + [l]

            currDict[s[l]] = currDict[s[l]] - 1
            if(currDict[s[l]] == 0):
                currDict.pop(s[l])

            l += 1
            r += 1
            if(r < len(s)):
                currDict[s[r]] = currDict.get(s[r], 0) + 1
        return(ans)
                