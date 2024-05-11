class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        res = []
        exists = {}
        for i, c in enumerate(s):
            exists[c] = i

        for i, c in enumerate(s):
            if c not in res:
                while res and c < res[-1] and exists[res[-1]] > i:
                    res.pop()
                        
                res.append(c)

        return ''.join(res)
    

"""
Had to look around a bit to get some help on this one.

The main trick:
- We should remove a letter already in the string if its larger then then next letter to be added and it appears later as well.
- Do this in reverse order res[-1] and not res[0]. This is because the existing res string is partially sorted already and thus
    it only works going backwards (as its not fully sorted due to the basis fo the question and going the other direction
    could be problematic e.g. bge where there is only one g in the whole string)
"""