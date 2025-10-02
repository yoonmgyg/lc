class Solution {
    public boolean partitionArray(int[] nums, int k) {
        int n = nums.length;
        if (k <= 0) return false;     
        if (n == 0) return false;      
        if (n % k != 0) return false;  

        int g = n / k;                 
        Map<Integer, Integer> freq = new HashMap<>();

        for (int x : nums) {
            int f = freq.getOrDefault(x, 0) + 1;
            if (f > g) return false;   
            freq.put(x, f);
        }
        return true;        
    }
}
