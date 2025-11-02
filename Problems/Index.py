class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        cite_count = [0] * (n + 1)
        for cite in citations:
            cite_count[min(cite, n)] += 1
        
        current_papers = 0
        for i in range(n, -1, -1):
            current_papers += cite_count[i]
            if current_papers >= i:
                return i
        
        return 0
