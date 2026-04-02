class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                height, j = stack.pop()
                maxArea = max(maxArea, height * (i - j))
                start = j
            stack.append((h,start))
        for (h,i) in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea