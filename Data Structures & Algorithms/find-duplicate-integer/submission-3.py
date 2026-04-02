class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for index in range(len(nums)):
            i = abs(nums[index]) - 1
            if nums[i] < 0:
                return i + 1
            nums[i] = nums[i] * -1
        return index
