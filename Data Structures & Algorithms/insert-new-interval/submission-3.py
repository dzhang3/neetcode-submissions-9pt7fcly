class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        if newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval]
        
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        
        overL,overR = 0,len(intervals)
        for i,interval in enumerate(intervals):
            if newInterval[0] > interval[1]:
                overL = i + 1
            if newInterval[1] < interval[0]:
                overR = i
                break
        
        
        s,e = newInterval
        if overL < overR:
            s = min(s,intervals[overL][0])
            e = max(e,intervals[overR - 1][1])
        # print(overL,overR)
        
        return intervals[:overL] + [[s,e]] + intervals[overR:]
            

