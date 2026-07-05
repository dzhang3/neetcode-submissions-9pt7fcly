"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        for i in intervals:
            events.append([i.start,1])
            events.append([i.end,-1])
        
        events.sort()
        cur = 0
        ans = 0
        for e in events:
            cur += e[1]
            ans = max(ans,cur)
        return ans
