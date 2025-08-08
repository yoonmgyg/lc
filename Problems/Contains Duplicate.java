class Solution {
    public boolean hasDuplicate(int[] nums) {
        // add numbers to set
        HashSet<Integer> mp = new HashSet<Integer>();
        for (int i = 0; i < nums.length; ++i) {
            // if not in set, add
            if (!mp.contains(nums[i])) {
                mp.add(nums[i]);
            } else { // if in set, return true
                return true;
            }
        }
        return false;
    }
}
