class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums) - 1
        while l < r:
            m = (l + r) // 2
            # print(l,r,m,nums[l],nums[r],nums[m])
            if nums[m] == target:
                return m
            if nums[l] > nums[m]:
                if target <= nums[m] or target >= nums[l]:
                    r = m
                else:
                    l = m + 1
            else:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m
        return l if nums[l] == target else -1