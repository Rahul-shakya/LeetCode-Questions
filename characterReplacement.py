class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        ans = 0
        charDict = {}
        while(r < len(s)):
            currChar = s[r]
            charDict[currChar] = charDict.get(currChar, 0) + 1
            currLen = r - l + 1
            cost = currLen - max(charDict.values())
            if(cost > k):
                charDict[s[l]] -= 1
                l += 1
            else:
                ans = max(ans, currLen)
            # print(f'{currChar} {charDict} {currLen} {cost} {ans}')
            r += 1
        return ans