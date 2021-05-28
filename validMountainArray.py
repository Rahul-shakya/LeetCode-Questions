from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        l = len(arr)
        if(l<3):
            return False
        if((arr[0] >= arr[1]) or (arr[l-1] >= arr[l-2])):
            return False            
        
        uphill = True
        for i in range(1,len(arr)-1):
            curr = arr[i]
            if(uphill == True):
                if(curr<arr[i+1]):
                    continue
                elif(curr == arr[i+1]):
                    return False
                else:
                    uphill = False
            else:
                if(curr > arr[i+1]):
                    continue
                elif(curr == arr[i+1]):
                    return False
                else:
                    return False
        return True

s = Solution()
answer = s.validMountainArray([1,2,3,6,5,3,1])
print(answer)
                
                
            
            
    