// https://leetcode.com/problems/generate-parentheses/description/

using namespace std;
#include <vector>

class Solution {
    vector<string> combos = vector<string>();

    void generateParenthesisRecursive(string base, int l, int r){
        if(l==0 && r==0){
            combos.push_back(base);
        } else {
            if(l > 0){
                generateParenthesisRecursive(base+"(",l-1,r);
            }

            if(r > 0 && l < r) {
                generateParenthesisRecursive(base+")",l,r-1);            
            }
        }
    }

    void resetCombos(){
        while(!combos.empty()){
            combos.pop_back();
        }
    }

public:
    vector<string> generateParenthesis(int n) {
        resetCombos();

        generateParenthesisRecursive("",n,n);
        return combos;
    }
};

/*
Time-space wise not efficent (O(2^N)) but still is optimal solution
Essentialy a BFS of all feasable combos
*/