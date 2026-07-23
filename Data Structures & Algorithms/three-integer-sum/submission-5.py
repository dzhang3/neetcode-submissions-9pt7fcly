class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        i = 0
        while i < n:
            l,r = i + 1,n - 1
            target = 0 - nums[i]
            print(i)
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    ans.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
            i += 1
            while i < n and nums[i] == nums[i - 1]:
                i += 1
                
        return ans
        