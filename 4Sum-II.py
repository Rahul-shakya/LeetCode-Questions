class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        tot = 0
        mapper = {}
        for i in range(0, len(nums1)):
            currA = nums1[i]
            for j in range(0,len(nums2)):
                currB = nums2[j]
                
                if( currA + currB not in mapper):
                    mapper[currA+currB] = 1
                else:
                    mapper[currA+currB]+=1
        
        for i in range(0, len(nums3)):
            currC = nums3[i]
            for j in range(0,len(nums4)):
                currD = nums4[j]
                ele = (currC + currD)*-1
                if( ele in mapper):
                    tot+=mapper[ele]
        
        return tot
