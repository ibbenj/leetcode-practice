class KthLargest {
    private PriorityQueue<Integer> testScores;
    private int queueSize;

    public KthLargest(int k, int[] nums) {
        testScores = new PriorityQueue<Integer>();
        queueSize = k;

        // Add all to heap
        for(int num : nums){
            testScores.add(num);
        }

        // Reduce heap size to top k elem
        while(testScores.size() > k){
            testScores.poll();
        }
    }
    
    public int add(int val) {
        testScores.add(val);

        // Reduce to top k entries
        if(testScores.size() > queueSize){
            testScores.poll();
        }
        
        return testScores.peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */