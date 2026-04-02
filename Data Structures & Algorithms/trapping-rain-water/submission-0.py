class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height) -1
        lm = [0] * len(height)
        rm = [0] * len(height)
        for i in range(len(height) - 1):
            lm[i + 1] = max(lm[i], height[i])
            rm[-(i+2)] = max(rm[-(i+1)],height[-(i+1)])
        total = 0
        for i, h in enumerate(height):
            total += max(0, min(lm[i],rm[i]) - h)
        return total



            
        