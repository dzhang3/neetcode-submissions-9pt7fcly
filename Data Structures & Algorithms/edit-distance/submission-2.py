class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        actions = [(1,1),(1,0),(0,1)]
        dp = [[-1] * (m + 1) for _ in range(n + 1)]
        def dfs(i,j):
            if dp[i][j] != -1:
                return dp[i][j]
            if i == n and j == m:
                dp[i][j] = 0
            elif i == n: 
                dp[i][j] = dfs(i,j + 1) + 1 # insert 
            elif j == m:
                dp[i][j] = dfs(i + 1,j) + 1 # delete
            elif word1[i] != word2[j]:
                ops = []
                if i < n and j < m:
                    ops.append(dfs(i+1,j+1)) # replace
                if i < n:
                    ops.append(dfs(i + 1,j)) # delete
                if j < m:
                    ops.append(dfs(i,j + 1)) # insert 
                dp[i][j] = min(ops) + 1
            else:
                dp[i][j] = dfs(i+1,j+1)
            return dp[i][j]
        return dfs(0,0)
        
            