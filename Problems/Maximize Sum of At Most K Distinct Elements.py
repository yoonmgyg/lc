class Solution {
    public int[] maxKDistinct(int[] nums, int k) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
        Set<Integer> numSet = new HashSet<>();
        for (int i = 0; i < nums.length; ++i) {
            if (!numSet.contains(nums[i])) {
                numSet.add(nums[i]);
                maxHeap.add(nums[i]);
            }
        }

        List<Integer> maxList = new ArrayList<>();
        for (int i = 0; i < k; ++i) {
            if (maxHeap.isEmpty()) {
                break;
            }
            maxList.add(maxHeap.poll());
        }

        int[] res = new int[maxList.size()];
        for (int i = 0; i < maxList.size(); ++i) {
            res[i] = maxList.get(i);
        }
        return res;
    }
}
