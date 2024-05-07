/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let prefix = "";

    for(let i=0; i<strs[0].length; i++){
        let nextPrefix = strs[0].slice(0,i+1);

        for(const str of strs){
            if(!str.startsWith(nextPrefix)){
                return prefix;
            }
        }

        prefix = nextPrefix;
    }

    return prefix;
};