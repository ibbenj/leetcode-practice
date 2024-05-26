// https://leetcode.com/problems/uncrossed-lines/

class Solution {
public:
    int maxUncrossedLines(vector<int>& nums1, vector<int>& nums2) {
        int mem[nums1.size()+1][nums2.size()+1];
        for(int i=0; i<nums1.size()+1; i++){
            for(int j=0; j<nums2.size()+1; j++){
                mem[i][j] = 0;
            }
        }

        for(int i=1; i<nums1.size()+1; i++){
            for(int j=1; j<nums2.size()+1; j++){
                if(nums1[i-1]==nums2[j-1]){
                    mem[i][j] = 1 + mem[i-1][j-1];
                } else {
                    mem[i][j] = mem[i-1][j] > mem[i][j-1] ? mem[i-1][j] : mem[i][j-1];
                }
            }
        }

        return mem[nums1.size()][nums2.size()];
    }
};

/*
Dynamic programming in O(nm)

I(i,j) is max matches where all of less than i in nums1 and less than j in nums2 is blocked
(as if we match num1[x] and nums2[y], we can't reuse any nums1 <=x or nums2 <= y as those ar blocked)

Use DP based on fact that I(i,j) = 1+I(i-1,j-1) if we have a match in i-1,j-1, else max(I(i-1,j),I(i,j-1))
*/