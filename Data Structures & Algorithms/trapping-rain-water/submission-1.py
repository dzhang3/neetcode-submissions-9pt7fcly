class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height) -1
        lm, rm = height[l], height[r]
        total = 0
        while l <= r:
            if lm < rm:
                lm = max(lm, height[l])
                total += lm - height[l]
                l += 1
            else:
                rm = max(rm, height[r])
                total += rm - height[r]
                r -= 1
        return total



            
        