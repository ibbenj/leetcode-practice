class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        for i in range(math.ceil(n/2)):
            for j in range(math.floor(n/2)):
                temp = matrix[j][i]
                matrix[j][i] = matrix[n-1-i][j]
                matrix[n-1-i][j] = matrix[n-1-j][n-1-i]
                matrix[n-1-j][n-1-i] = matrix[i][n-1-j]
                matrix[i][n-1-j] = temp

# Do one floor and one ceil to handle when n is odd (as
# we ceiled twice we would rotate the middle row/col twice
# instead of once)