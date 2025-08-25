class Solution {
    public int findMin(int[] nums) {
        int left = 0, right = nums.length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[right]) {
                left = mid + 1;   // min is in right half
            } else {
                right = mid;      // min is in left half (including mid)
            }
        }
        return nums[left]; // left points to min
    }
}
