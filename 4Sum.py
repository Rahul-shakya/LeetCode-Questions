class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums)<4:
            return []
        

        #Without using hashmaps. Complexity - O(n3)

        res = []
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                sum2 = nums[i]+nums[j]
                left = j + 1
                right = len(nums)-1
                while(left < right):
                    sumTot = sum2 + nums[left] + nums[right]
                    if(sumTot == target and [nums[i],nums[j],nums[left],nums[right]] not in res):
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        left+=1
                        right-=1
                    elif sumTot < target:
                        left+=1
                    else:
                        right-=1
        
        return res
