/*
Time: O(n) - as constant amount of change provided
Space: O(1)
*/


class Solution {
    public boolean lemonadeChange(int[] bills) {
        // Num of bills in register
        int[] billsCnt = {0, 0}; // 5, 10 (keeping track of 20s is useless as can't use it as change)

        for(int bill : bills){
            int change = bill-5;

            // Take bill
            if(bill==5){
                billsCnt[0]++;
            } else if (bill==10){
                billsCnt[1]++;
            }

            // Provide Change
            while(change>=10 && billsCnt[1] > 0){
                billsCnt[1]--;
                change-=10;
            }

            while(change>0){
                if(billsCnt[0]==0){
                    return false;
                }
                billsCnt[0]--;
                change-=5;
            }
        }

        return true;
    }
}