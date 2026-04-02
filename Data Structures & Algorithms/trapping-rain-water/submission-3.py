class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height) - 1
        maxL, maxR = 0,0
        ans = 0
        while l <= r:
            # print(l,r,ans, maxL, maxR)
            if maxL < maxR:
                ans += max(0,min(maxL,maxR) - height[l])
                maxL = max(maxL,height[l])
                l += 1
            else:
                ans += max(0,min(maxL,maxR) - height[r])
                maxR = max(maxR,height[r])
                r -= 1
        return ans

          