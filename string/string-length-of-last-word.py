# https://leetcode.com/problems/length-of-last-word/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index = -1
        while len(s)+index >= 0 and s[index] == ' ':
            index -= 1

        cnt = 0
        while len(s)+index >= 0 and s[index] != ' ':
            index -= 1
            cnt += 1

        return cnt
        