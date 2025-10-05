class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        current = s
        paren = k * "(" + k * ")"
        removed = current.replace(paren, "")
        while current != removed:
            current = removed
            removed = current.replace(paren, "")

        return removed
        
