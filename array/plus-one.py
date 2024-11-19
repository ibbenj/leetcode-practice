# https://leetcode.com/problems/plus-one/?envType=problem-list-v2&envId=array
# Runtime: O(n) 
# Space: O(1)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[len(digits)-1] += 1
        for i in range(0,len(digits)):
            index = len(digits)-1-i

            if(digits[index]<=9):
                break

            digits[index] = 0

            if i == len(digits)-1:
                digits.insert(0,1)
            else:
                digits[index-1] += 1

        return digits