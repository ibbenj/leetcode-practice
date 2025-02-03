// Time + Space: O(n) for string length n

class Solution {
    public int numDecodings(String s) {
        int size = s.length();

        int[] numDecode = new int[size+1]; // +1 for base
        numDecode[0] = 1; // Used as base to avoid accessing index -1
        if(s.charAt(0) == '0'){
            return 0; // String has no valid encoding
        }
        numDecode[1] = 1; // this is for index 0 in char

        for (int i=1; i<size; i++) {
            int lastChr = s.charAt(i) - '0';
            int secLastChr = s.charAt(i-1) - '0';

            if(lastChr != 0){
                if(secLastChr == 1 || (secLastChr == 2 && lastChr <= 6)){
                    numDecode[i+1] = numDecode[i] + numDecode[i-1];
                } else {
                    numDecode[i+1] = numDecode[i];
                }
            } else {
                if (secLastChr == 1 || secLastChr == 2) {
                    numDecode[i+1] = numDecode[i-1];
                } else {
                    return 0; // String has no valid encoding
                }
            }
        }

        return numDecode[size];
    }
}

// N(i) = num of ways to decode string from indexes 0 to i
// N(i) = sum{N(i-1), N(i-2)} -  assuming that both cases are valid encodings (between 1 and 26 so no 0,27,28,...) - if
// invalid coding, than exclude that option from the sum above. If no valid options return 0 as impossible to encode entire
// string