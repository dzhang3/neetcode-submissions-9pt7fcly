class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total / 2
        
        memo = {}
        def dfs(cursum,i):
            if cursum == target:
                memo[i,cursum] = True
                return True
            if i == len(nums):
                memo[i,cursum] = False
                return False
            
            if (i+1,cursum) in memo:
                exc = memo[i+1,cursum]
            else:
                exc = dfs(cursum,i+1)
            if (i+1,cursum + nums[i]) in memo:
                inc = memo[i+1,cursum + nums[i]]
            else:
                inc = dfs(cursum + nums[i],i+1)
            memo[i,cursum] = exc or inc
            return exc or inc
        res = dfs(0,0)
        return res
            