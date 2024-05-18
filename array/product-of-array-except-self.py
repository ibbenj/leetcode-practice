# https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = 0
        for num in nums:
            if num == 0:
                zeroCount += 1

        product = 1
        if zeroCount > 1:
            product = 0
        else:
            for num in nums:
                if num != 0:
                    product *= num  

        answer = []
        for i in range(len(nums)):
            if nums[i] == 0:
                answer.append(product)
            elif zeroCount == 1:
                answer.append(0)
            else:
                newProd = product/nums[i]
                answer.append(round(newProd))

        return answer
    
# Main challange was accounting for special case where 1 or more 0s exist in array