from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_area = 0
        while(left < right):
            curr_area = min(height[left],height[right]) * (right-left)
            if(curr_area > max_area):
                max_area = curr_area
            if(height[left] < height[right]):
                left = left + 1
            else:
                right = right - 1
        return max_area

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
