class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def dfs(i,j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0 # reached end of s without hitting match
            count = dfs(i+1,j) # skip
            if s[i] == t[j]:
                count += dfs(i+1,j+1) # include
            return count
        return dfs(0,0)