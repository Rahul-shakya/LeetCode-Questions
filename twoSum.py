from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = {}    #map key:element value:index
        n = len(nums)
        
        for i in range(n):
            y = target - nums[i]
            if(y in mapper):
                return [mapper[y],i]
            else:
                mapper[nums[i]] = i

s = Solution()
print(s.twoSum([1,2,6,4,5,7],3))
