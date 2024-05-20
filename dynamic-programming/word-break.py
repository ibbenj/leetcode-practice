# https://leetcode.com/problems/word-break/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        isSegementable = [] # Stores if a substring up to index i is valid substring collection

        for i in range(len(s)):
            isSegementable.append(False)
            for word in wordDict:
                if i+1>=len(word) and s[i-len(word)+1:i+1] == word:
                    # If substring covers entire string so far, or before it is an accepted substring from our memory,
                    # then our current string keeps it true for now
                    if len(word) == len(isSegementable) or (len(word)<=len(isSegementable) and isSegementable[len(isSegementable)-1-len(word)]):
                        isSegementable[-1] = True
                        break

        return isSegementable[-1]
        
# O(nm) time using dynamic programming