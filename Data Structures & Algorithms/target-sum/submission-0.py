class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i,a):
            if i == len(nums):
                if a == target:
                    return 1
                else:
                    return 0
    
            count = 0
            count += dfs(i + 1,a - nums[i])
            count += dfs(i + 1,a + nums[i])
            return count
        return dfs(0,0)