class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            currA = nums[i]
            left = i+1
            right = len(nums)-1
            while(left < right):
                if((currA + nums[left] + nums[right]) == 0 and [currA,nums[left],nums[right]] not in res):
                    res.append([currA,nums[left],nums[right]])
                    left+=1
                    right-=1
                elif((currA + nums[left] + nums[right]) < 0):
                    left+=1
                else:
                    right-=1
        return res
