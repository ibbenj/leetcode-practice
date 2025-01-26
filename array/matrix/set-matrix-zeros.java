import java.util.*;
// https://leetcode.com/problems/set-matrix-zeroes/?envType=problem-list-v2&envId=array

// Time: O(nm)
// Space: O(1)
class Solution {
    public void setZeroes(int[][] matrix) {
        HashSet<Integer> markedCols = new HashSet<Integer>();
        HashSet<Integer> markedRows = new HashSet<Integer>();

        // Mark all rows/columns with zeros
        for(int i=0; i<matrix.length; i++){
            for(int j=0; j<matrix[0].length; j++){
                if(matrix[i][j] == 0){
                    markedCols.add(i);
                    markedRows.add(j);
                }
            }
        }

        // Update all respective rows / columns
        for (int col : markedCols) {
            for (int row=0; row<matrix[0].length; row++){
                matrix[col][row] = 0;
            }
        }
        for (int row : markedRows) {
            for (int col=0; col<matrix.length; col++){
                matrix[col][row] = 0;
            }
        }
    }
}