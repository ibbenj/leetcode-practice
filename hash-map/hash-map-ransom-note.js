/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    const map = new Map()
    for(const letter of magazine){
        if(!map.has(letter)){
            map.set(letter,0)
        }

        const letterCnt = map.get(letter);
        map.set(letter,letterCnt+1)
    }

    for(const letter of ransomNote){
        const letterCnt = map.get(letter);

        if(!letterCnt || letterCnt == 0){
            return false;
        }

        map.set(letter,letterCnt-1)
    }

    return true;
};