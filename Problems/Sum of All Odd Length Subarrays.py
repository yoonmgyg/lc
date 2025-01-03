# Gets odd subarrays and adds to sum if current count is less than array
class Solution:
    def sumOddLengthSubarrays(self, arr):
        total = 0
        for i in range(1, len(arr)+1 ,2):
            j = 0
            count = i
            while count <= len(arr):
                total += sum(arr[j:count])
                j += 1
                count += 1
        return total
