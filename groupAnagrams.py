class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            d[sorted_s].append(s)
        
        return d.values()        


    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        mainDict = {}
        ans = []
        for currStr in strs:
            currSorted = ''.join(sorted(currStr))
            if currSorted not in mainDict:
                mainDict[currSorted] = [] + [currStr]
            else:
                mainDict[currSorted] = mainDict[currSorted] + [currStr]
        return mainDict.values()

    # slowest
    def groupAnagrams3(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}
        ana = []
        for word in strs:
            hashed = ''.join(sorted(word))
            if hashed in groups:
                groups[hashed].append(word)
            else:
                groups[hashed] = [word]
                
        for li in groups.values():
            ana.append(li)
        return ana
