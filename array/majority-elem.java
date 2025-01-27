class Solution {
    // Time: O(n)
    // Space: O(n)
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> elemCnt = new HashMap<>();

        for (int i=0; i<nums.length; i++) {
            // Add entry to elemCnt if not existant
            if(!elemCnt.containsKey(nums[i])){
                elemCnt.put(nums[i], 0);
            }

            // Increment entry in elemCnt
            int cnt = elemCnt.get(nums[i]);
            elemCnt.put(nums[i], cnt+1);
        }

        // Return max of keys
        for (Map.Entry<Integer, Integer> elem : elemCnt.entrySet()) {
            if(elem.getValue() > nums.length/2){
               return elem.getKey(); 
            }
        }
        return -1;
    }
}