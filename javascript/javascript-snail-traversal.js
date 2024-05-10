/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function(rowsCount, colsCount) {
    // Bounds check
    if (this.length !== rowsCount * colsCount){
        return [];
    }

    let res = [];
    for(let i=0; i<rowsCount; i++){
        res.push([]);
    }

    let i=0;
    while(i<this.length){
        for(let j=0; j<rowsCount; j++){
            res[j].push(this[i]);
            i++;
        }

        if(i==this.length){
            break;
        }

        for(let j=0; j<rowsCount; j++){
            res[rowsCount-1-j].push(this[i]);
            i++;
        }
    }

    return res;
}

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */