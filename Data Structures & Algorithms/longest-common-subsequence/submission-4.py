class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) > len(text1):
            tmp = text1
            text1 = text2
            text2 = tmp
        n = len(text1)
        m = len(text2)
        # bottom up dp
        # traverse from the back, dp[i][j] represents longest subseq at text1[i], text2[j]
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n - 1,-1,-1):
            for j in range(m-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        return max(dp[0])