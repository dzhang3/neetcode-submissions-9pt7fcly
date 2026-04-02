class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        i =0
        while i < (len(nums) - 2):
            l,r = i + 1, len(nums) - 1
            t = nums[i]
            while l < r:
                if nums[l] + nums[r] == -t:
                    ans.append([t, nums[l], nums[r]])
                    while l < r and nums[r - 1] == nums[r]:
                        r -= 1
                    r -= 1
                    while l < r and nums[l + 1] == nums[l]:
                        l += 1
                    l += 1
                elif nums[l] + nums[r] < -t:
                    while l < r and nums[l + 1] == nums[l]:
                        l += 1
                    l += 1
                else:
                    while l < r and nums[r - 1] == nums[r]:
                        r -= 1
                    r -= 1
            while i < (len(nums) - 2) and nums[i + 1] == nums[i]:
                i += 1
            i += 1
        return ans