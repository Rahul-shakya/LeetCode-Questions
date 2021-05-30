from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arraySum = 0
        for i in nums:
            arraySum += i
        n = len(nums)
        totSum = n * (n+1) // 2
        missingNum = totSum - arraySum
        return missingNum


    def missingNumber2(self, nums: List[int]) -> int:

        n = len(nums)
        totXor = 0
        for i in range(n+1):
            totXor = totXor ^ i

        for i in nums:
            totXor = totXor ^ i

        return totXor

s = Solution()
print(s.missingNumber([3,0,1]))
print(s.missingNumber2([3,0,1]))