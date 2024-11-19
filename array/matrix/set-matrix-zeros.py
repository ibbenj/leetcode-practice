# https://leetcode.com/problems/set-matrix-zeroes/description/?envType=problem-list-v2&envId=array

# Runtime: O(n*m)
# Space: O(n+m)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        xAxis = []
        for column in matrix:
            hasZero = False
            for item in column:
                if item == 0:
                    hasZero = True
                    break
            
            xAxis.append(hasZero)

        yAxis = []
        for i in range(0,len(matrix[0])):
            hasZero = False
            for j in range(0,len(matrix)):
                if matrix[j][i] == 0:
                    hasZero = True
                    break
                
            yAxis.append(hasZero)     

        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if xAxis[i] or yAxis[j]:
                    matrix[i][j] = 0                


        
