class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin, curMax = 1,1
        gMax = max(nums)
        
        for num in nums:
            tmp = curMin * num
            curMin = min(tmp,curMax * num,num)
            curMax = max(tmp,curMax * num,num)
            gMax = max(gMax,curMax)
        return gMax