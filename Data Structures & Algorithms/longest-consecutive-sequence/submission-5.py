

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hn = set(nums)
        ans = 0
        for n in nums:
            if n - 1 not in hn:
                a = n + 1
                while a in hn:
                    a += 1
                ans = max(ans, a - n)
        return ans