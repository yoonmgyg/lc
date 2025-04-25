class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1]+nums[2]

        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1

            while left < right:
                currSum = nums[i] + nums[left] + nums[right]

                if currSum == target:
                    return target

                if abs(currSum-target) < abs(closest-target):
                    closest = currSum
                
                if target>currSum:
                    left += 1
                else:
                    right -= 1
        return closest
