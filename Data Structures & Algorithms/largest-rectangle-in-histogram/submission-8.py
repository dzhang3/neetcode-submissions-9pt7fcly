class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        pre = [0] * n
        stack = [(-1,-1)]
        for i,h in enumerate(heights):
            while stack[-1][1] >= h:
                stack.pop()
            pre[i] = stack[-1][0]
            stack.append((i,h))
        post = [0] * n
        stack = [(n,-1)]
        for i in range(n-1,-1,-1):
            h = heights[i]
            while stack[-1][1] >= h:
                stack.pop()
            post[i] = stack[-1][0]
            stack.append((i,h))

        # print(pre,post)
        ans = 0
        for i in range(n):
            ans = max(ans,heights[i] * (post[i] - pre[i] - 1))
        return ans

        
        
        
                