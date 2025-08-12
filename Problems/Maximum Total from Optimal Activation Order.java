class Solution {
    public long maxTotal(int[] value, int[] limit) {
        long max = 0;
        
        Map<Integer, PriorityQueue<Integer>> limitMap = new HashMap<>(); // use priority queue to get highest value with each limit
        for (int i = 0; i < value.length; ++i) {
            limitMap.computeIfAbsent(limit[i], k -> new PriorityQueue<Integer>(Collections.reverseOrder())).offer(value[i]);
        }

        for (Map.Entry<Integer, PriorityQueue<Integer>> e : limitMap.entrySet()) { 
            PriorityQueue<Integer> pq = e.getValue();
            for (int i = 0; i < e.getKey() && !pq.isEmpty(); ++i) {  // loop through each limit's priority queue to sum limit elements
                max += pq.poll();
            }
        }

        return max;
    }
}
