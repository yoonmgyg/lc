# Gets the GCD by looping through nums with min and max element, finding what is divisible with both
def findGCD(self, nums: List[int]) -> int:
    small = min(nums)
	  large = max(nums)
		for i in range(small, 0, -1):
			  if small % i == 0 and large % i == 0:
				    return i
