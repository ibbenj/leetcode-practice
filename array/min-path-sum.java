// https://leetcode.com/problems/minimum-path-sum/?envType=problem-list-v2&envId=array
// Time: O(mn) - dynamic programming question
class Solution {
    public int minPathSum(int[][] grid) {
        int width = grid.length;
        int height = grid[0].length;

        int[][] minGrid = new int[width][height];
        for(int i=0; i<width; i++){
            for(int j=0; j<height; j++){
                minGrid[i][j] = Integer.MAX_VALUE;
            }
        }
        minGrid[0][0] = grid[0][0];

        for(int i=0; i< width; i++){
            for(int j=0; j< height; j++){
                if(i+1 < width){
                    minGrid[i+1][j] = Math.min(minGrid[i][j]+grid[i+1][j], minGrid[i+1][j]);
                }

                if(j+1 < height){
                    minGrid[i][j+1] = Math.min(minGrid[i][j]+grid[i][j+1], minGrid[i][j+1]);
                }
            }
        }

        return minGrid[width-1][height-1];
    }
}