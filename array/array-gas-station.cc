class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int netCost = 0;
        for(int i=0; i<cost.size(); i++){
            netCost += cost[i];
        }

        int netGas = 0;
        for(int i=0; i<gas.size(); i++){
            netGas += gas[i];
        }

        if(netCost>netGas){
            return -1;
        }

        // Since we have proven that at least 1 starting point exists that can do
        // the round trip, let's go in order. If we find that starting at x index
        // y gets us blocked, we also know that all indexes from x to y-1 can't work as
        // we have the same problem. So we can just start from y and reset. Note that
        // we don't need to check the loop back to index 0, b/c as we have proven
        // at least 1 index must work

        int tank = 0;
        int start = 0;
        for(int i=0;i<gas.size(); i++){
            tank += gas[i] - cost[i];
            if(tank < 0){
                start = i+1;
                tank = 0;
            }
        }

        return start;
    }
};

// Time: O(n)
// Space: O(1)
// That was a very neat problem. I like how it uses the fact that if you prove at least 1 solution exists,
// then we don't have to backtran from index n-1 to index 0.