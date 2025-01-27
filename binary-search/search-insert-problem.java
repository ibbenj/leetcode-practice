// Time: O(log(n))
// Space: O(1)

class Solution {
    public int searchInsert(int[] nums, int target) {
        int start = 0;
        int end = nums.length-1;
        int i = -1; // dummy value
        
        // bin search
        while(start <= end){
            i = (start + end) / 2; // find medium
            if(nums[i] < target){
                start = i+1;
            } else if (nums[i] > target) {
                end = i-1;
            } else { // nums[i] == target
                return i;
            }
        }
        return start;
    }
}