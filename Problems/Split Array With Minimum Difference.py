class Solution:
    def splitArray(self, nums: List[int]) -> int:
        min_diff = float('inf')
        left_sum = 0
        left_inc = True
        for right in range(1, len(nums)):
            if not left_inc:
                break
            if nums[right] <= nums[right-1]:
                left_inc = False

            left_sum += nums[right-1]
            right_sum = 0

            valid = True
            for right_end in range(right, len(nums)):
                if right_end != right and nums[right_end] >= nums[right_end-1]:
                    valid = False
                    break
                right_sum += nums[right_end]

            if valid:
                min_diff = min(min_diff, abs(left_sum - right_sum))
            
        return -1 if min_diff == float('inf') else min_diff
