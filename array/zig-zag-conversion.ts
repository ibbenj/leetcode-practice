// https://leetcode.com/problems/zigzag-conversion/description/?envType=study-plan-v2&envId=top-interview-150

function convert(s: string, numRows: number): string {
    let formatted = "";

    for(let i=0; i<numRows; i++){
        let j=i;
        while(j<s.length){
            formatted += s[j];

            if(i!=0 && i!= numRows-1){
                j += 2*(numRows - i - 1);
                if(j<s.length){
                    formatted += s[j];
                    j += 2*i;
                }
            } else {
                j += numRows;

                if(numRows >= 3){
                    j += numRows - 2;
                }
            }
        }
    }

    return formatted;
};

/*
O(n)

This was challenging from the perspective of coming up with a mathematical formula
to use.
*/