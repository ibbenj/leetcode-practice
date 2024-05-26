# https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''
        Do not return anything, modify board in-place instead.
        '''
        row = len(board)
        col = len(board[0])

        def testSafe(board: List[List[str]], i, j):
            if i >= 0 and j >= 0 and i < row and j < col:
                if board[i][j] == 'O':
                    board[i][j] = 'S'

                    testSafe(board,i+1,j)
                    testSafe(board,i-1,j)
                    testSafe(board,i,j+1)
                    testSafe(board,i,j-1)

        for i in range(row):
            testSafe(board,i,0)
            testSafe(board,i,col-1)

        for j in range(col):
            testSafe(board,0,j)
            testSafe(board,row-1,j)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'S':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

        
# O(nm) time and O(1) space
# It's easier to search for non-captured 'O's than captured 'O's (just search perimeter of map and then do DFS for each one).
# In this case we add a third state 'S' (safe) to track non-captured 'O's, then after finding all of these, we convert all 'O's to
# 'X's (captured) and all 'S's to 'O's