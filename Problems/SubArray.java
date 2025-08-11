public class SubArray {
    public int[] sub(int[] nums, int start, int end){
        int[] res = new int[end - start]; // get length of subarray
        int resIndex = 0;
        for (int i = start; i < end; ++i) { // loop from start to end
            res[resIndex] = nums[i];
            resIndex++;
        }
        return res;
    }
}
