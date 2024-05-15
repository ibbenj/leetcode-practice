class TrieNode {
    constructor(data, isEnd) {
        this.data = data
        this.next = new Map() 
        this.isEnd = isEnd               
    }
}

class Trie {
    constructor() {
        this.start = new TrieNode(null,false);
    }

    /** 
    * @param {string} word
    * @return {void}
    */
    insert = function(word) {
        let curNode = this.start;
        
        for(let i=0; i<word.length; i++){
            const letter = word[i];
            
            if(!curNode.next.get(letter)){
                const newNode = new TrieNode(letter,i+1 == word.length);
                curNode.next.set(letter, newNode)
            } else if (i+1 == word.length){
                const nextNode = curNode.next.get(letter);
                nextNode.isEnd = true;
                curNode.next.set(letter, nextNode);
            }

            curNode = curNode.next.get(letter);
        }    
    };

    /** 
    * @param {string} word
    * @return {boolean}
    */
    search = function(word) {
        let curNode = this.start;
        
        for(const letter of word){
            curNode = curNode.next.get(letter);

            if(!curNode){
                return false;
            }
        }

        return curNode.isEnd;
    };

    /** 
    * @param {string} prefix
    * @return {boolean}
    */
    startsWith = function(prefix) {
        let curNode = this.start;
        
        for(const letter of prefix){
            curNode = curNode.next.get(letter)

            if(!curNode){
                return false;
            }
        }

        return true;
    };

    /** 
    * Your Trie object will be instantiated and called as such:
    * var obj = new Trie()
    * obj.insert(word)
    * var param_2 = obj.search(word)
    * var param_3 = obj.startsWith(prefix)
    */
}