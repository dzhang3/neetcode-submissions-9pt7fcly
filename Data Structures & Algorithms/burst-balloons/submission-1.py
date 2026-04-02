class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[-1] * n for _ in range(n)]
        def dfs(l,r): 
            if r < l:
                return 0
            if dp[l][r] != -1:
                return dp[l][r]
            maxCoin = 0
            for i in range(l,r + 1):
                coin = nums[l-1] * nums[i] * nums[r+1]
                coin += dfs(l,i-1) + dfs(i+1,r)
                maxCoin = max(maxCoin,coin)
            dp[l][r] = maxCoin
            return maxCoin
        return dfs(1,len(nums)-2)
            
            
            