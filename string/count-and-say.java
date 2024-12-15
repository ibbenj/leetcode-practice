/*
 * Time: O(n) ** Can I assume that the stirng's size doesn't scale at a constant/linear rate? I think that's fine
 * Also use stringbuilder as faster than string (builds string in spot instead of reallocaitng memoryf or each adjustment in size)
 */

class Solution {
    public String countAndSay(int n) {
        if (n == 1){
            return "1";
        }

        String prev = countAndSay(n-1);

        StringBuilder rle = new StringBuilder();
        int i=0;
        while(i < prev.length()){
            char digit = prev.charAt(i);
            int cnt = 0;
            while(i < prev.length() && digit == prev.charAt(i)){
                cnt += 1;
                i += 1;
            }

            rle.append(cnt);
            rle.append(digit);
        }

        return rle.toString();
    }
}



/*
1
11
21
1211
111221
312211
13112221
*/