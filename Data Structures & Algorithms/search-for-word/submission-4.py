class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
    
        def traverse(i,j,c,seen):
            if i < 0 or i >= n or j < 0 or j >= m or board[i][j] != word[c] or (i,j) in seen:
                return False
            if c == len(word) - 1:
                return True
            seen.add((i,j))
            wordMatch = False
            for x,y in dirs:
                wordMatch = traverse(i + x, j + y, c + 1,seen) or wordMatch
            seen.remove((i,j))
            return wordMatch
        
        for i in range(n):
            for j in range(m):
                seen = set()
                if board[i][j] == word[0] and traverse(i,j,0,seen):
                    return True
        return False
