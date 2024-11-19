/**
 * @param {number} n
 * @return {number}
 */
var rotatedDigits = function(n) {
    const isGood = (num) => {
        return [2,5,6,9].includes(num);
    }

    const isValid = (num) => {
        return [0,1,2,5,6,8,9].includes(num);
    }

    let good = 0;
    const mem = [];
    for(let i=0; i<n; i++){
        const num = i+1;

        if(num>=10){
            const ones = num % 10;
            const digits = (num - ones) / 10;
            if(isValid(ones) && mem[digits-1]>=1){
                if(isGood(ones) ||  mem[digits-1]==2){
                    mem.push(2);
                    good += 1;
                } else {
                    mem.push(1);
                }
            } else {
                mem.push(0);
            }
        } else {
            if(isGood(num)){
                good += 1;
                mem.push(2);
            } else if (isValid(num)){
                mem.push(1);
            } else {
                mem.push(0);
            }
        }
    }
    
    return good;
};

console.log(rotatedDigits(5))