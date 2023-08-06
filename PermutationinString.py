class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1) > len(s2)):
            return False
        l = 0
        r = len(s1) - 1
        targetDict = {}
        for currChar in s1:
            targetDict[currChar] = targetDict.get(currChar, 0) + 1
        
        currDict = {}
        for i in range(r+1):
            currDict[s2[i]] = currDict.get(s2[i], 0) + 1

        while(r < len(s2)):
            if(currDict == targetDict):
                return True
            currToDelete = s2[l]
            currDict[currToDelete] -= 1
            if(currDict[currToDelete] == 0):
                currDict.pop(currToDelete)
            l += 1
            r += 1

            if(r < len(s2)):
                currDict[s2[r]] = currDict.get(s2[r], 0) + 1
        
        return False

