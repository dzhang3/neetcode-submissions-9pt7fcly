class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        ans = []
        for i in range(len(nums)):
            if not queue:
                queue.append((nums[i],i))
            else:
                while queue and nums[i] > queue[-1][0]:
                    queue.pop()
                queue.append((nums[i],i))
            while queue and queue[0][1] < i - k + 1:
                queue.popleft()
            if i >= k - 1:
                ans.append(queue[0][0])
        return ans