class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        print(count)
        length = len(nums)
        for i in nums:
            if(count[i] > int(length/2)):
                return i
