#https://leetcode.com/problems/number-of-islands/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandCnt = 0
        
        def explore(i,j):
            grid[i][j] = 0
            if i+1 < len(grid) and grid[i+1][j] == "1":
                explore(i+1,j)
            
            if j+1 < len(grid[0]) and grid[i][j+1] == "1":
                explore(i,j+1)           

            if i-1 >= 0 and grid[i-1][j] == "1":
                explore(i-1,j)
            
            if j-1 >= 0 and grid[i][j-1] == "1":
                explore(i,j-1)    


        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                if grid[i][j] == "1":
                    islandCnt += 1
                    explore(i,j)

        return islandCnt
    
"""
This was a clever and fun one! (also got runtime beats 98%! and memory 81%).

We do a search of the matrix for an island, and when we get to it, we call explore() to run a BFS to turn all the island's values into 0.
This is so when we get back to searching for the next island we face no duplicates.

Space-complexity: O(1)

Time-complexity: You may think O(n^2m^2) because of the explore inside a double for loop, however when you think about it the explore
is guarenteed to only iterte through each element in the matrix one time only. So it's rather O(nm+nm)=O(nm). Neat!
"""