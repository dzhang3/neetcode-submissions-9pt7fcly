class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre, post = [nums[0]] * n,[nums[-1]] * n

        for i in range(1,n):
            pre[i] = pre[i-1] * nums[i]
            post[-(i + 1)] = post[-i] * nums[-(i + 1)]
        # print(pre,post)
        ans = []
        for i in range(n):
            a = pre[i - 1] if i > 0 else 1
            b = post[i + 1] if i < n - 1 else 1
            ans.append(a*b)
        return ans