class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        ans = 0
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                ph,pi = stack.pop()
                ans = max(ans, ph * (i - pi))
                start = pi
            # print(ans)
            stack.append((h,start))
        
        for h,s in stack:
            ans = max(ans,h * (n - s))
        return ans

        
        
        
                