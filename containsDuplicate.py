class Solution:
    #using map
    def containsDuplicate1(self, nums: List[int]) -> bool:
        count = {}
        
        for i in nums:
            if(i in count):
                count[i] = count[i] + 1
            else:
                count[i] = 1
            if(count[i] > 1):
                return True
        return False

    #using Set
    def containsDuplicate2(self, nums: List[int]) -> bool:
        count = set()
        for num in nums:
            if(num in count):
                return True
            else:
                count.add(num)
        return False
