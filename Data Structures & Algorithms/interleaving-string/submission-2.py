class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        dp = {}
        def dfs(i,j,k):
            if (i,j) in dp:
                return dp[i,j]
            if i == len(s1) and j == len(s2) and k == len(s3):
                return True
            t1 = False
            t2 = False
            if i < len(s1) and s1[i] == s3[k]:
                t1 = dfs(i + 1,j,k + 1)
            if j < len(s2) and s2[j] == s3[k]:
                t2 = dfs(i,j + 1, k + 1)
            dp[i,j] = t1 or t2
            return t1 or t2
        return dfs(0,0,0)

            