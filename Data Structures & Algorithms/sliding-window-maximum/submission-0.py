class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        l = r = 0

        while r < len(nums):
            while len(q) > 0 and q[-1] < nums[r]:
                q.pop()
            q.append(nums[r])

            if r - l + 1 == k:
                res.append(q[0])
                if q[0] == nums[l]:
                    q.popleft()
                l += 1
            r += 1
        return res
        
