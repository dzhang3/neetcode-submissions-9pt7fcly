class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        dp = {}
        def dfs(i,j):            
            if (i,j) in dp:
                return dp[i,j]
                
            if i == n and j == m:
                return True
            elif j == m:
                return False
            elif i == n:
                return j == (m - 2) and p[j + 1] == '*'
            
            
            if j < (m - 1) and p[j + 1] == '*':
                exc = dfs(i,j+2) # doesn't include current character
                inc = False
                if s[i] == p[j] or p[j] == '.':
                    inc = dfs(i+1,j)   # does include current character
                dp[i,j] = exc or inc
            elif s[i] != p[j] and p[j] != '.':
                dp[i,j] = False
            else: 
                dp[i,j] = dfs(i+1,j+1)
            return dp[i,j]
        return dfs(0,0)

        