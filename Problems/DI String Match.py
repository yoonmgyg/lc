# Loop through string and append based on I and D, returning the smallest perm
def diStringMatch(self, s: str) -> List[int]:
        arr = []
        smallest, largest = 0, len(s)
		
        for i in range(len(s)):
            if s[i] == 'I':
                arr.append(smallest)
                smallest += 1
            else:
                arr.append(largest)
                largest -= 1
				
        arr.append(smallest)
        return arr
