/*
Note that time and space are both O(1) because the Sudoku is of fixed size!

Also I read that a more efficient way to do this is to use bit masking (so 000000000 instead of a set).
Just food for thought :)
 */

 import java.util.*;

 class Solution {
    public boolean isValidSudoku(char[][] board) {
        int length = board.length;
        int width = board[0].length;

        Set<Character> usedNums = new HashSet<Character>();

        // Vertical checks
        for(int i=0; i<length; i++){
            for(int j=0; j<width; j++){
                char curSpace = board[i][j];

                if(curSpace != '.'){
                    if(usedNums.contains(curSpace)){
                        return false;
                    }
                    usedNums.add(curSpace);
                }
            }
            usedNums.clear();
        }

        // Horizontal checks
        for(int j=0; j<width; j++){
            for(int i=0; i<length; i++){
                char curSpace = board[i][j];

                if(curSpace != '.'){
                    if(usedNums.contains(curSpace)){
                        return false;
                    }
                    usedNums.add(curSpace);
                }
            }
            usedNums.clear();
        }

        // Sub-boxes checks
        for(int i=0; i<length/3; i++){
            for(int j=0; j<width/3; j++){
                // For each sub-box
                int xOffset = i*3;
                int yOffset = j*3;
                for(int x=xOffset; x<xOffset+length/3; x++){
                    for(int y=yOffset; y<yOffset+width/3; y++){
                        char curSpace = board[x][y];

                        if(curSpace != '.'){
                            if(usedNums.contains(curSpace)){
                                return false;
                            }
                            usedNums.add(curSpace);
                        }
                    }
                }
                
                usedNums.clear();
            }
        }

        return true;
    }
}