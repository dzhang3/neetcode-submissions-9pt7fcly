class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(curAmt,i):
            if curAmt == amount:
                dp[curAmt,i] = 1
                return 1
            if curAmt > amount:
                dp[curAmt,i] = 0
                return 0
            if (curAmt,i) in dp:
                return dp[curAmt,i]
            
            count = 0
            for j in range(i,len(coins)):
                count += dfs(curAmt + coins[j],j)
            dp[curAmt,i] = count
            return dp[curAmt,i]
        return dfs(0,0)