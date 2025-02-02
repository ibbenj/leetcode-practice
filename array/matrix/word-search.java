/*
 * Rememer: arrays passed in functions as pointers (Shallow copies) - must keep in mind when resetting it
 * Time: O(m*n*4^word.length) - worst case is start at each space and get to finial char and isn't there (we explore 4 options at each level so 4^word.length)
 * Space: O(word.length) due to recursion
 */

class Solution {
    private boolean recSearch(char[][] board, String word, int i, int j) {
        // Check valid location
        if(i<0 || i>=board.length || j<0 || j>=board[0].length){
            return false;
        }

        // Check if char matches
        char nextChar = word.charAt(0);
        if(board[i][j] != nextChar){
            return false;
        }

        // Marked as explored
        char temp = board[i][j];
        board[i][j] = '-';

        // Check if next word is empty (i.e. word exists)
        String nextWord = word.substring(1);
        if(nextWord.length() == 0){
            return true;
        }

        // Check each direction 
        if(recSearch(board, nextWord, i-1, j) || recSearch(board, nextWord, i+1, j) || recSearch(board, nextWord, i, j-1) || recSearch(board, nextWord, i, j+1)){
            return true;
        }

        board[i][j] = temp;
        return false;
    }

    public boolean exist(char[][] board, String word) {
        if(word.length() == 0){
            return true;
        }

        for(int i=0; i<board.length; i++){
            for(int j=0; j<board[0].length; j++){
                if(recSearch(board, word, i, j)){
                    return true;
                }
            }
        }
        return false;
    }
}