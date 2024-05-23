# https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        max_area = 0

        while l < r:
            max_area = max(max_area,min(height[r],height[l])*(r-l))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
        return max_area
    
"""
Interesting problem. You start at outer ends of array (as it maximizes the width), and only move inwards if the loss of width is overset by the gain in height.
"""