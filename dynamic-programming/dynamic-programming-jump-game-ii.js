/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    let minJumps = 0;
    let curMaxReachable = 0;
    let maxReachable = 0;

    for(let i=0;i<nums.length;i++){
        if(curMaxReachable < i){
            minJumps += 1;
            curMaxReachable = maxReachable;
        }

        if(maxReachable < i + nums[i]){
            maxReachable = i + nums[i];
        }
    }

    return minJumps;
};