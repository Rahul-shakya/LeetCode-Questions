class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = dict()
        left = 0
        right = 0
        maxLength = 0
        n = len(s)
        while(left < n and right < n):
            curr = s[right]
            if (curr in charMap):
                left = max(left,charMap[curr]+1)
            charMap[curr]=right
            
            if((right-left+1) > maxLength):
                maxLength = right-left+1
            right = right + 1
        return maxLength
        

s = Solution()
length = s.lengthOfLongestSubstring("abcaxywzaabbc")
print(length)

# longest string being "bcaxywz" length = 7 
