class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[-1] * m for _ in range(n)]
        def dfs(i,j):
            if dp[i][j] != -1:
                return dp[i][j]
            dirs = [1,1,1,1]
            if i > 0 and matrix[i-1][j] > matrix[i][j]:
                dirs[0] = dfs(i-1,j) + 1
            if i < (n - 1) and matrix[i+1][j] > matrix[i][j]:
                dirs[1] = dfs(i+1,j) + 1
            if j > 0 and matrix[i][j-1] > matrix[i][j]:
                dirs[2] = dfs(i,j-1) + 1
            if j < (m - 1) and matrix[i][j+1] > matrix[i][j]:
                dirs[3] = dfs(i,j + 1) + 1
            dp[i][j] = max(dirs)
            return dp[i][j]
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(dfs(i,j),ans)
        return ans
        
            