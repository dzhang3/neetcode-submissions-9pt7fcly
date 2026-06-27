class Solution:
    def jump(self, nums: List[int]) -> int:
        r = 0
        steps = 0
        newR = 0
        for i,j in enumerate(nums):
            if i > r:
                steps += 1
                r = newR
            newR = max(newR, i + j)
        return steps
        