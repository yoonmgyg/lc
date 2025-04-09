class Solution:
	def defangIPaddr(self, address: str) -> str:
		ans = []
		for ch in address:
			if ch.isdigit():
				ans.append(ch)
			else:
				ans.append("[.]")

		return "".join(ans)
