class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for c in coins:
                if i - c >= 0:
                    if i == c:
                        dp[i] = 1
                        break
                    else:
                        if dp[i-c] == -1:
                            continue
                        if dp[i] == -1:
                            dp[i] = dp[i-c] + 1
                        dp[i] = min(dp[i],dp[i-c] + 1)
        return dp[-1]
