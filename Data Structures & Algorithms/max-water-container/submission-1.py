class Solution:
    def maxArea(self, h: List[int]) -> int:
        l,r = 0, len(h) - 1
        maxArea = 0
        while l < r:
            maxArea = max(maxArea, (r - l) * min(h[l],h[r]))
            if h[r] < h[l]:
                r -= 1
            else:
                l += 1
        return maxArea

        