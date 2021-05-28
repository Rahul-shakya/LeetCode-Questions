from typing import List

class Solution:
    def searchRange1(self, nums: List[int], target: int) -> List[int]:    # better approach, modified binary search approach
        left =0
        right = len(nums)-1
        curr=0
        l = []

        # finding left most target :

        while(left <= right):
            mid = int((left+right)/2)
            if(nums[mid] == target):
                if(mid == 0 or nums[mid-1] != target):
                    l.append(mid)
                right = mid - 1
            elif(nums[mid] < target):
                left = mid+1
            else:
                right = mid -1

        left = 0
        right = len(nums)-1
        curr = 0

        #finding right most target :

        while(left <= right):
            mid = int((left+right)/2)
            if(nums[mid] == target):
                if(mid == ( len(nums)-1) or nums[mid+1] != target):
                    l.append(mid)
                    break
                left = mid + 1
            elif(nums[mid] < target):
                left = mid + 1
            else:
                right = mid - 1
        if(len(l) == 0):
            return [-1,-1]
        else:
            return l
    
    def searchRange2(self, nums: List, target: int) -> List[int]:   # not so better approach, used the concept of slicing 
        try:
            start = nums.index(target)
            end = len(nums) - nums[::-1].index(target) - 1
        except:
            start = -1
            end = -1
        li = [start,end]
        return li

s = Solution()

print(s.searchRange1([1,2,3,5,5,5,5,5,7,8,9,],5))

print(s.searchRange2([1,2,3,5,5,5,5,5,7,8,9,],5))
