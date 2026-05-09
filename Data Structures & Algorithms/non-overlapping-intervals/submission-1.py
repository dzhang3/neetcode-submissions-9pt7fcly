class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # initial thoughts:
        # go through and just remove if overlapping, but can't guarantee minimum intervals
        # backtrack: for every interval, we either remove or don't remove
        # if keep, remove every interval that overlaps with it 
        # first sort everything
        # minimize removal / maximize keep
        # can memoize it?
        # dp[i][j] represents last time something was added
        # dp[i][j] = max()
        # [[1,2],[1,4],[2,4]]
        intervals = sorted(intervals)
        preEnd = intervals[0][1]
        ans = 0
        for s, e in intervals[1:]:
            if s < preEnd:
                preEnd = min(preEnd,e)
                ans += 1
            else:
                preEnd = e
        return ans 