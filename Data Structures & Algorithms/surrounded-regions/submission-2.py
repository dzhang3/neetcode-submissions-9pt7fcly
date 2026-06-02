class Solution:
    def solve(self, board: List[List[str]]) -> None:
        r,c = len(board),len(board[0])
        visited = [[False] * c for _ in range(r)]
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]
        def dfs(i,j):
            visited[i][j] = True
            for dx, dy in dirs:
                if i + dx >= 0 and i + dx < r and j + dy >= 0 and j + dy < c and not visited[i + dx][j + dy] and board[i + dx][j + dy] == 'O':
                    dfs(i + dx,j + dy)
        
        for i in range(r):
            if board[i][0] == 'O':
                dfs(i,0)
            if board[i][c - 1] == 'O':
                dfs(i,c - 1)
        
        for j in range(c):
            if board[0][j] == 'O':
                dfs(0,j)
            if board[r - 1][j] == 'O':
                dfs(r-1,j)
    
        
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O' and not visited[i][j]:
                    board[i][j] = 'X'
        

            