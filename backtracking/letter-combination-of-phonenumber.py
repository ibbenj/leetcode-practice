# https://leetcode.com/problems/letter-combinations-of-a-phone-number/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    combos = []

    keyMap = {2:97,3:100,4:103,5:106,6:109,7:112,8:116,9:119}

    def combosRecursive(self, curString, digits):
        if len(digits) == 0:
            if len(curString) > 0:
                self.combos.append(curString)
        else:
            nextDigit = digits[0]
            digits = digits[1:]

            asciiVal = self.keyMap.get(int(nextDigit))

            keyRange = 3
            if (asciiVal == 112 or asciiVal == 119):
                keyRange = 4

            for letter in range(asciiVal,asciiVal+keyRange):
                nextString = curString + chr(letter)
                self.combosRecursive(nextString,digits)

    def letterCombinations(self, digits: str) -> List[str]:
        while len(self.combos) > 0:
            self.combos.pop()

        self.combosRecursive("",digits)
        return self.combos
        
"""
LOOKING AROUND AFTER: FOUND THIS SOLUTION WHICH IS MUCH BETTER IN TERMS OF SIMPLICITY AS WELL AS PUTTING HTE FUNCTION
INSIDE OF THE OTHER FUNCTION (BY ACCOUNT cohesk)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        
        def backtrack(combination, next_digits):
            if not next_digits:
                res.append(combination)
                return
            
            for letter in phone[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])
        
        backtrack("", digits)
        return res
"""