# https://leetcode.com/problems/find-peak-element/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            if right-left == 1:
                return right if nums[right] > nums[left] else left
            elif right-left == 0:
                return left

            i = floor((left+right)/2)

            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
            elif nums[i] < nums[i+1]:
                left = i
            else:
                right = i

        return -1