// https://leetcode.com/problems/h-index/?envType=study-plan-v2&envId=top-interview-150

/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {
    n = citations.length;
    const arr = new Array(n+1).fill(0);

    // Increment corresponding buckets
    citations.map((citation)=>{
        if(citation > n){
            arr[n]++;
        } else {
            arr[citation]++;
        }
    })

    // Go backwards and find best h-index
    let cumulative = 0;
    for(let i=n; i>=0; i--){
        cumulative += arr[i];
        if(cumulative>=i){
            return i;
        }
    }
    return 0;
};

// O(n) - interesting question. You essentialy sort it in O(n) using O(n) space complexity