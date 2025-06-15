class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        tested_count = 0

        for device in batteryPercentages:
            tested_count += int(max(0, device - tested_count) > 0)

        return tested_count
