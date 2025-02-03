class Solution {
    public int myAtoi(String s) {
        // Remove leading whitespace
        while (s.length() > 0 && s.charAt(0) == ' ') {
            s = s.substring(1);
        }

        if (s.length() == 0){
            return 0;
        }

        boolean isPositive = !(s.charAt(0) == '-');
        if (s.charAt(0) == '+' || s.charAt(0) == '-'){
            s = s.substring(1);
        }

        long res = 0;
        while (s.length() > 0 && Character.isDigit(s.charAt(0))) {
            res *= 10;
            res += s.charAt(0) - '0';

            s = s.substring(1);

            if (isPositive) {
                if (res > Integer.MAX_VALUE) {
                    return Integer.MAX_VALUE;
                }
            } else {
                if (res*-1 < Integer.MIN_VALUE) {
                    return Integer.MIN_VALUE;
                }
            }
        }

        if (!isPositive) {
            res *= -1;
        }

        return (int)res;
    }
}