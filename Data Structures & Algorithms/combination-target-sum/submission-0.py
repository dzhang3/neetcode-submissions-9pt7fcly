class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def combinations(i,total,adds):
            if total == target:
                ans.append(adds)
                return
            elif total > target or i == len(nums):
                return
            combinations(i + 1,total,adds)
            combinations(i,total + nums[i],adds + [nums[i]])
            
        combinations(0,0,[])
        return ans