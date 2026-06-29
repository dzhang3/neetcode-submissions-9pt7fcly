class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)

        ans = []
        cl,cr = intervals[0]
        for l,r in intervals[1:]:
            if l > cr:
                ans.append([cl,cr])
                cl,cr = l,r
            else:
                cr = max(cr,r)
        ans.append([cl,cr])
        return ans