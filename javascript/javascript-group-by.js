/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    const map = new Map();
    this.map((item)=>{
        const key = fn(item);
        if(!map.has(key)){
            map.set(key,[]);
        }
        const arr = map.get(key);
        arr.push(item);
        map.set(key,arr);
    });
    return Object.fromEntries(map);
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */

// Saw in solutions tab after doing it an interesting solution
// using reduce to carry the resulting value through each iteration
// instead of what I did with map