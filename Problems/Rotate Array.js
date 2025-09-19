var rotate = function(nums, k) {
    k %= nums.length;
    var reverse = function(left, right) {
        while (left < right) {
            [nums[left], nums[right]] = [nums[right], nums[left]]
            left++;
            right--; 
        }
    }

    reverse(0, nums.length - 1);
    reverse(0, k - 1);
    reverse(k, nums.length - 1);

};
