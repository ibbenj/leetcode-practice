"""
https://leetcode.com/problems/convert-1d-array-into-2d-array/description/?envType=problem-list-v2&envId=matrix
Runtime: O(n*m)
Space: O(n*m)
Improvements: Can splice array and push that to the outer list in ans, instead of doing each entry individually
"""

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []
        
        ans = [[None for _ in range(n)] for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                ans[i][j] = original[i*n+j]

        return ans
        