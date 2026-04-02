class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i,buying):
            if (i,buying) in dp:
                return dp[i,buying]
            if i >= len(prices):
                dp[i,buying] = 0
                return 0
            skip = dfs(i + 1,buying) # skip
            if not buying: # we are looking to sell
                sell = dfs(i + 2,True) + prices[i] #sell
                dp[i,buying] = max(sell,skip)
                return max(sell,skip)
            else: #ps >= pb we are looking to buy
                buy = dfs(i + 1,False) - prices[i]
                dp[i,buying] = max(buy,skip)
                return max(buy,skip)
        return dfs(0,True)