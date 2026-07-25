class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre = [0] * n
        post = [0] * n
        for i in range(1,n):
            pre[i] = max(pre[i-1],height[i-1])
            post[-(i + 1)] = max(post[-(i)],height[-i])
        ans = 0
        # print(pre,post)
        for i in range(1,n - 1):
            ans += max(min(pre[i],post[i]) - height[i],0)
            print(max(min(pre[i],post[i]) - height[i],0))
        return ans
