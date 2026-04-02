class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dfs(i,cursum,pb,ps):
            if i >= len(prices):
                return cursum
            if ps < pb: # we are looking to sell
                #if prices[i] > prices[pb]: #if there's a profit
                profit = prices[i] - prices[pb]
                sell = dfs(i + 2,cursum + profit,pb,i) #sell
                skip = dfs(i + 1,cursum,pb,ps) # skip
                return max(sell,skip)
            else: #ps >= pb we are looking to buy
                buy = dfs(i + 1, cursum,i,ps)
                skip = dfs(i + 1,cursum,pb,ps)
                return max(buy,skip)


        return dfs(0,0,-1,-1)