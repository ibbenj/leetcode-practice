/*
Just quick set practice
Time: O(n)
Space: O(n)
*/

import java.util.*;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> existsAlready = new HashSet<>();
        for(int num : nums) {
            if (!existsAlready.add(num)) {
                return true;
            }
        }

        return false;
    }
}