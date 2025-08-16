class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums); // sort array to match sum
      
        for (int i = 0; i < nums.length; i++) { // loop through each number for possiuble sums
            if (i > 0 && nums[i] == nums[i-1]) { // skip repeating numbers
                continue;
            }
            
            int j = i + 1; 
            int k = nums.length - 1;

            while (j < k) { // find all sums between i and k
                int total = nums[i] + nums[j] + nums[k];

                if (total > 0) {
                    k--;
                } else if (total < 0) {
                    j++;
                } else {
                    res.add(Arrays.asList(nums[i], nums[j], nums[k])); // add if sum is found
                    j++;

                    while (nums[j] == nums[j-1] && j < k) {
                        j++;
                    }
                }
            }
        }
        return res;        
    }
}
