class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[0] = 0
        for i,jump in enumerate(nums):
            for j in range(1,jump + 1):
                if i + j < n:
                    if dp[i + j] == -1:
                        dp[i + j] = dp[i] + 1 
                    else:
                        dp[i + j] = min(dp[i + j],dp[i] + 1)
        return dp[n-1]
        