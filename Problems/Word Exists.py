class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def backtrack(r, c, current, word):
            next_ch = word[len(current)]    
            if board[r][c] != next_ch:
                return False

            current += next_ch
            if current == word:
                return True

            ch = board[r][c]
            board[r][c] = "#"
            found = False
            for dr, dc in dir:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    found = found or backtrack(nr, nc, current, word)
                
            board[r][c] = ch
            return found
        
        found = False
        for i in range(m):
            for j in range(n):
                found = found or backtrack(i, j, "", word)
        
        return found
