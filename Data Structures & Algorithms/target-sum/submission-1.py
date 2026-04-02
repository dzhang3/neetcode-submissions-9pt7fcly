class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(i,a):
            if (i,a) in dp:
                return dp[i,a]
            if i == len(nums):
                if a == target:
                    return 1
                else:
                    return 0
    
            count = 0
            count += dfs(i + 1,a - nums[i])
            count += dfs(i + 1,a + nums[i])
            dp[i,a] = count
            return count
        return dfs(0,0)