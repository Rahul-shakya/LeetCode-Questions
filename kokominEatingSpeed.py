import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def condition(piles: List[int], rate):
            totHours = 0
            for currPile in piles:
                totHours += math.ceil(currPile/rate)
            return totHours
        ans = -1
        left, right = 1, max(piles)
        while(left <= right):
            mid = left + (right-left)//2
            currHours = condition(piles, mid)
            if(currHours > h):
                left = mid + 1
            else:
                right = mid - 1
                ans = mid
                
        return ans
            