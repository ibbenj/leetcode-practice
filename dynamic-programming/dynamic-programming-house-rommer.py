# https://leetcode.com/problems/house-robber/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def rob(self, nums: List[int]) -> int:
        maxMoney = []
        for i, houseVal in enumerate(nums):
            if i == 0:
                maxMoney.append(houseVal)
            elif i == 1:
                maxMoney.append(max(houseVal,maxMoney[0]))
            else:
                maxMoney.append(max(maxMoney[i-1],houseVal+maxMoney[i-2]))

        return maxMoney[-1]
        