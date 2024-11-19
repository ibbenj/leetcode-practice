"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9
"""


# 0 2 3 4 5
# [4,3,1,2,0]

def numPair(nums, target):
    numMap = {}

    for i, num in enumerate(nums):
        numMap[num] = i

        pairVal = target-num
        if pairVal in numMap.keys():
            return [i,numMap[pairVal]]
        
    return False


print(numPair([3,2,7,7],5))
print(numPair([7,4,3,6],5))