# https://leetcode.com/problems/rotate-array/submissions/1257113533/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for _ in range(k%len(nums)):
            temp = nums.pop()
            nums.insert(0,temp)

"""
At least for python I overthought this question at first :)
"""