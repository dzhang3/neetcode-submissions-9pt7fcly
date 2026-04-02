class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def getsubsets(i,subset):
            if i == len(nums):
                ans.append(subset)
                return
            getsubsets(i + 1,subset + [nums[i]])
            getsubsets(i + 1,subset)
        getsubsets(0,[])
        return ans