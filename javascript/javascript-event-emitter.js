class EventEmitter {
    constructor() {
        this.subMap = new Map();
    }
    
    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */
    subscribe(eventName, callback) {
        if(!this.subMap.has(eventName)){
            this.subMap.set(eventName,[]);
        }
        const callbacks = this.subMap.get(eventName);
        callbacks.push(callback);
        this.subMap.set(eventName,callbacks);
        
        return {
            unsubscribe: () => {
                let callbacks = this.subMap.get(eventName);
                callbacks = callbacks.filter((fn) => {
                    return fn != callback;
                });
                this.subMap.set(eventName,callbacks);               
            }
        };
    }
    
    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
    emit(eventName, args = []) {
        let res = []
        const callbacks = this.subMap.get(eventName);
        if(callbacks){
            for(const callback of callbacks){
                // Must do .apply() rather than calling the function, otherwise it passes the arguments as strings instead of numbers
                res.push(callback.apply(null,args));
            }
        }

        return res;
    }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */