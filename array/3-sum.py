"""
NOTE: I DIDN'T GET TO FINISH THIS PROBLEM BUT RIGHT O(N^2) IDEA.

Basically you know that the three values should sum to 0 (e.g. x+y+z=0). We can rewrite
this as x+y=-z, and then use features like a hashmap to turn this from a O(n^3) problem
into a O(n^2) problem.

I still need to figure out how to remove duplicate answers without adding additional
complexity. TBD

"""


#https://leetcode.com/problems/3sum/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pairs = {}

        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i != j:
                    if -(num1+num2) not in pairs.keys():
                        pairs[-(num1+num2)] = [[i,j]]
                    else:
                        curPairs = pairs[-(num1+num2)]
                        curPairs.append([i,j])
                        pairs[-(num1+num2)] = curPairs

        triplets = []
        for i, num in enumerate(nums):
            if num in pairs.keys():
                possiblePairs = pairs[num]
                for posPair in possiblePairs:
                    if i != posPair[0] and i != posPair[1]:
                        arr = [nums[posPair[0]], nums[posPair[1]], nums[i]]
                        arr.sort()
                        triplets.append(arr)

        return list(triplets)