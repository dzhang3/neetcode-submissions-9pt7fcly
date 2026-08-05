class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        ans = 0
        for i in range(n):
            mh = heights[i]
            ans = max(ans,mh)
            for j in range(i + 1,n):
                mh = min(mh,heights[j])
                ans = max(ans,mh * (j - i + 1))
        return ans
                