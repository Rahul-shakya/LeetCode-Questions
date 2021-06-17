# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:

# One approach can be stright brute force which would obviously give timeouts for large values of n

# Variation 1 of binary search :
 def firstBadVersion1(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while(left < right):
            mid = left + int((right-left)/2)
            if( isBadVersion(mid) ):
                right = mid
            else:
                left = mid + 1
        return left
        

# Variation 2 of binary search (This approach is slightly faster than the upper one(4 ms faster lol): 

    def firstBadVersion2(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        if(isBadVersion(left)):
            return left
        
        while(left < right):
            mid = left + int((right-left)/2)
            if( isBadVersion(mid) and isBadVersion(mid-1) == False ):
                return mid
            elif(isBadVersion(mid) == False):
                left = mid + 1
            else:
                right = mid
                
        return left
        
