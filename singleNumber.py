from typing import List

class Solution:

    def singleNumber(self, nums: List[int]) -> int:

        ans = 0
        for i in nums:
            ans = ans ^ i   #XOR Operation

        return ans

s = Solution()
print(s.singleNumber([1,1,2,2,8,3,3,4,4,5,5]))
    




