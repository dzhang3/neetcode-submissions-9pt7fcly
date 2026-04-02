class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i,n in enumerate(heights):
            start = i
            while stack and stack[-1][0] > n:
                h,j = stack.pop()
                maxArea = max(maxArea, h * (i - j))
                start = j
            stack.append((n,start))
        
        for (height, start) in stack:
            maxArea = max(maxArea, height * (len(heights) - start))
        
        return maxArea
        


            
        