class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[-1] * len(t) for _ in range(len(s))]
        def dfs(i,j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0 # reached end of s without hitting match
            if dp[i][j] != -1:
                return dp[i][j]
            count = dfs(i+1,j) # skip
            if s[i] == t[j]:
                count += dfs(i+1,j+1) # include
            dp[i][j] = count
            return dp[i][j]
        return dfs(0,0)