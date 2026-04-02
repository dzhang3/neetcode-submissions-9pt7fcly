class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProd = [1] * (len(nums))
        rightProd = [1] * (len(nums))

        for i in range(0,len(nums)):
            leftProd[i] = nums[i] * (leftProd[i-1] if i > 0 else 1)
            rightProd[-(i+1)] = nums[-(i+1)] * (rightProd[-(i)] if i > 0 else 1) 

        ans = []
        for i in range(0,len(nums)):
            l = 1 if i == 0 else leftProd[i-1]
            r = 1 if i == len(nums) - 1 else rightProd[i + 1]
            ans.append(l * r)
        return ans

        