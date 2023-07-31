class Solution:
    # O(Nlog(N)) using sorting
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0
        nums = list(set(nums))
        nums.sort()
        print(nums)
        ans = 1
        currMax = 1
        for i in range(len(nums)-1):
            if((nums[i]+1) == nums[i+1]):
                currMax += 1
            else:
                if(currMax > ans):
                    ans = currMax
                currMax = 1
        return(max(ans, currMax)) 

    
    def longestConsecutive2(self, nums: List[int]) -> int:
        ans = 0
        setOfNums = set(nums)
        for currNum in nums:
            currMax = 1
            if((currNum - 1) in setOfNums):
                continue
            else:
                currNum += 1
                while(currNum in setOfNums):
                    currMax += 1
                    currNum += 1
            ans = max(currMax, ans)
        return ans
