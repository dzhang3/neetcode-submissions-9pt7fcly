class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        lo = prices[0]
        for p in prices:
            lo = min(lo,p)
            ans = max(ans,p - lo)
        return ans